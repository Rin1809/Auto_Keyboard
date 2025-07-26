# core/workers.py
import time
from PySide6.QtCore import QObject, Signal, Slot, QThread
from pynput.keyboard import Controller as PynputController, Listener as PynputListener, Key as PynputKey, KeyCode
from .translations import Translations

# --- Ham tien ich lay ten hien thi cho Pynput Key ---
def get_pynput_key_display_name(key_obj):
    try:
        if isinstance(key_obj, PynputKey): # Phim dac biet
            name = key_obj.name
            name_map = {
                'alt_l': 'Alt', 'alt_r': 'Alt', 'alt_gr': 'AltGr',
                'ctrl_l': 'Ctrl', 'ctrl_r': 'Ctrl',
                'shift_l': 'Shift', 'shift_r': 'Shift',
                'cmd': 'Cmd', 'cmd_r': 'Cmd', # Mac/Win key
                'enter': 'Enter', 'space': 'Space', 'tab': 'Tab',
                'esc': 'Esc', 'delete': 'Del', 'backspace': 'Backspace',
                'up': 'Up', 'down': 'Down', 'left': 'Left', 'right': 'Right',
                'page_up': 'PgUp', 'page_down': 'PgDn',
                'home': 'Home', 'end': 'End', 'insert': 'Ins',
                'caps_lock': 'CapsLock', 'num_lock': 'NumLock',
                'print_screen': 'PrtSc', 'scroll_lock': 'ScrollLock', 'pause': 'Pause',
                **{f'f{i}': f'F{i}' for i in range(1, 25)},
                **{ # Media keys, etc.
                    'media_play_pause': 'Play/Pause', 'media_volume_mute': 'Mute',
                    'media_volume_up': 'VolUp', 'media_volume_down': 'VolDown',
                    'media_previous': 'PrevTrack', 'media_next': 'NextTrack',
                    'menu': 'Menu', 'apps': 'AppsKey'
                }
            }
            return name_map.get(name, name.capitalize())
        elif hasattr(key_obj, 'char') and key_obj.char is not None: # Phim ky tu (tu KeyCode)
            return str(key_obj.char).upper()
        elif isinstance(key_obj, str): # Neu la chuoi (ky tu don gian)
             return key_obj.upper()
        else: # Ko xac dinh
            return "Unknown"
    except Exception: # Neu co loi
        return "ErrorKey"

# --- Worker gõ phím ---
class AutoTyperWorker(QObject):
    update_status_signal = Signal(str)
    typing_finished_signal = Signal()
    error_signal = Signal(str)
    def __init__(self, text_to_type, interval_ms, repetitions, hotkey_display_name):
        super().__init__()
        self.text_to_type = text_to_type
        self.interval_s = interval_ms / 1000.0
        self.repetitions = repetitions
        self.hotkey_display_name = hotkey_display_name
        self.keyboard_controller = PynputController()
        self._is_running_request = True
    @Slot()
    def run(self):
        error_emitted = False # Flag theo doi loi
        try:
            if not self.text_to_type:
                self.error_signal.emit(Translations.get("worker_empty_text_error"))
                error_emitted = True; return
            if self.interval_s <= 0:
                self.error_signal.emit(Translations.get("worker_invalid_interval_error"))
                error_emitted = True; return
            if self.repetitions < 0:
                self.error_signal.emit(Translations.get("worker_invalid_repetitions_error"))
                error_emitted = True; return

            count = 0; initial_delay = 0.75; start_time = time.perf_counter()
            while time.perf_counter() - start_time < initial_delay:
                if not self._is_running_request:
                    return 
                time.sleep(0.05)

            while self._is_running_request:
                if self.repetitions != 0 and count >= self.repetitions: break
                special_keys_map = {
                    "<enter>": PynputKey.enter, "<tab>": PynputKey.tab, "<esc>": PynputKey.esc,
                    "<space>": PynputKey.space, "<up>": PynputKey.up, "<down>": PynputKey.down,
                    "<left>": PynputKey.left, "<right>": PynputKey.right,
                    **{f"<f{i}>": getattr(PynputKey, f"f{i}") for i in range(1, 13)},
                }

                if not self._is_running_request: break

                if self.text_to_type.lower() in special_keys_map:
                    key_to_press = special_keys_map[self.text_to_type.lower()]
                    self.keyboard_controller.press(key_to_press)
                    time.sleep(0.03) 
                    self.keyboard_controller.release(key_to_press)
       
                else:
                    for char in self.text_to_type:
                        if not self._is_running_request:
                            break
                        self.keyboard_controller.press(char)
                        time.sleep(0.03) 
                        self.keyboard_controller.release(char)
                        time.sleep(0.02) 
                
                if not self._is_running_request: break

                count += 1
                rep_text = f"{self.repetitions}" if self.repetitions != 0 else Translations.get("rep_text_infinite")

                self.update_status_signal.emit(Translations.get("worker_status_running",
                    count=count, rep_text=rep_text, hotkey_display_name=self.hotkey_display_name
                ))
                sleep_start_time=time.perf_counter()
                while time.perf_counter()-sleep_start_time < self.interval_s:
                    if not self._is_running_request:break
                    time.sleep(0.05)
                if not self._is_running_request:break
        except Exception as e:
            self.error_signal.emit(Translations.get("worker_runtime_error", error_message=str(e)))
            error_emitted = True
        finally:
            if not error_emitted:
                self.typing_finished_signal.emit()
    @Slot()
    def request_stop(self): self._is_running_request=False

# --- Worker lắng nghe Hotkey ---
class HotkeyListenerWorker(QObject):
    hotkey_pressed_signal=Signal()
    def __init__(self,hotkey_to_listen):
        super().__init__()
        self.hotkey_to_listen=hotkey_to_listen
        self._pynput_listener=None
        self._keep_listening=True
    @Slot()
    def run(self):
        def on_press(key):
            if not self._keep_listening:return False
            try:
                # So sanh key object truc tiep
                if key == self.hotkey_to_listen:
                    self.hotkey_pressed_signal.emit()
                # So sanh char neu hotkey la ky tu don gian va key cung la ky tu (tu KeyCode)
                elif isinstance(self.hotkey_to_listen, str) and \
                     hasattr(key, 'char') and key.char is not None and \
                     key.char.lower() == self.hotkey_to_listen.lower():
                     self.hotkey_pressed_signal.emit()

            except AttributeError:pass
            except Exception: pass
            return self._keep_listening

        try:
            self._pynput_listener=PynputListener(on_press=on_press, suppress=False)
            self._pynput_listener.start()
            self._pynput_listener.join()
        except Exception:
            pass

    @Slot()
    def request_stop(self):
        self._keep_listening=False
        if self._pynput_listener and self._pynput_listener.is_alive():
            try:
                self._pynput_listener.stop()
            except Exception:
                try:
                    # Pynput co the co race condition khi stop, thu cach khac
                    PynputListener.stop(self._pynput_listener)
                except Exception:
                    pass # Bo qua neu ko stop dc ngay
        self._pynput_listener = None

# --- Worker lắng nghe một phím duy nhất (cho cài đặt hotkey) - DA DUOC UPDATE ---
class SingleKeyListenerWorker(QObject):
    key_captured_signal = Signal(int, object, str) # hotkey_type, Pynput key object, key name string
    error_signal = Signal(int, str) # hotkey_type, error_message
    # Bao hieu listener da ket thuc (bat duoc phim, loi hoac huy) cho hotkey_type tuong ung
    listener_operation_finished_signal = Signal(int)

    def __init__(self):
        super().__init__()
        self._pynput_listener_instance = None
        self._current_hotkey_type_being_set = 0 # Loai hotkey dang duoc set
        self._is_actively_listening_for_key = False # Flag dieu khien pynput listener con
        self._keep_worker_thread_running = True # Flag dieu khien vong lap chinh cua worker (run())

    @Slot(int)
    def activate_listener_for_hotkey_type(self, hotkey_type_to_set):
        # Kich hoat worker de bat dau lang nghe cho mot loai hotkey cu the
        if self._is_actively_listening_for_key:
            return
        self._current_hotkey_type_being_set = hotkey_type_to_set
        self._is_actively_listening_for_key = True

    @Slot()
    def cancel_current_listening_operation(self):
        if self._is_actively_listening_for_key:
            self._is_actively_listening_for_key = False
            if self._pynput_listener_instance and self._pynput_listener_instance.is_alive():
                try:
                    self._pynput_listener_instance.stop()
                except Exception:
                    pass

    def _on_press_capture_key(self, key_pressed):
        if not self._is_actively_listening_for_key:
            return False

        try:
            # Neu key_pressed la KeyCode (vd: 'a'), dung key_pressed.char cho hotkey
            # Neu la Key (vd: Key.f9), dung key_pressed
            actual_key_obj_for_hotkey = key_pressed
            if isinstance(key_pressed, KeyCode) and key_pressed.char is not None:
                 # Neu muon luu char ('a') thay vi KeyCode object cho hotkey, thi gan:
                 # actual_key_obj_for_hotkey = key_pressed.char
                 # Tuy nhien, de get_pynput_key_display_name xu ly dong nhat, cu de KeyCode
                 pass


            key_name_str = get_pynput_key_display_name(actual_key_obj_for_hotkey)
            if key_name_str == "Unknown" or key_name_str == "ErrorKey":
                self.error_signal.emit(self._current_hotkey_type_being_set, Translations.get("msgbox_error_set_hotkey_text", error_message=f"Phím không nhận diện: {actual_key_obj_for_hotkey}"))
            else:
                self.key_captured_signal.emit(self._current_hotkey_type_being_set, actual_key_obj_for_hotkey, key_name_str)
        except Exception as e:
            self.error_signal.emit(self._current_hotkey_type_being_set, Translations.get("msgbox_error_set_hotkey_text", error_message=str(e)))
        finally:
            self._is_actively_listening_for_key = False
            return False # Stop listener sau khi bat duoc phim

    @Slot()
    def run(self):
        while self._keep_worker_thread_running:
            if self._is_actively_listening_for_key:
                active_hotkey_type_at_start = self._current_hotkey_type_being_set
                try:
                    # suppress=True de phim dat hotkey ko bi type vao ung dung khac
                    self._pynput_listener_instance = PynputListener(on_press=self._on_press_capture_key, suppress=True)
                    self._pynput_listener_instance.start()
                    self._pynput_listener_instance.join()
                except Exception as e:
                    if self._is_actively_listening_for_key : # Check neu van dang active thi moi emit loi
                        self.error_signal.emit(active_hotkey_type_at_start, Translations.get("msgbox_error_set_hotkey_text", error_message=f"Lỗi bộ lắng nghe: {str(e)}"))
                        self._is_actively_listening_for_key = False # Dam bao reset flag
                finally:
                    # Du co loi hay khong, listener da ket thuc (join() thoat)
                    self._is_actively_listening_for_key = False # Reset flag
                    self._pynput_listener_instance = None # Xoa instance
                    self.listener_operation_finished_signal.emit(active_hotkey_type_at_start) # Bao hieu ket thuc
            else:
                QThread.msleep(50) # Sleep neu ko active

    @Slot()
    def request_stop_worker_thread(self): # Goi khi dong ung dung
        self._keep_worker_thread_running = False
        self._is_actively_listening_for_key = False # Huy neu dang lang nghe
        if self._pynput_listener_instance and self._pynput_listener_instance.is_alive():
            try:
                self._pynput_listener_instance.stop()
            except Exception:
                pass
        self._pynput_listener_instance = None


# --- Worker ghi thao tác bàn phím ---
class KeyboardRecorderWorker(QObject):
    # key_obj, key_name_display, action_canonical ("press"/"release"), delay_ms
    key_event_recorded = Signal(object, str, str, float)
    recording_status_update = Signal(str)
    recording_finished = Signal()

    def __init__(self, start_record_hotkey, stop_record_hotkey_name): # start_record_hotkey khong con dung
        super().__init__()
        # self.start_record_hotkey = start_record_hotkey # Khong can nua, hotkey xu ly o main_window
        self.stop_record_hotkey_name = stop_record_hotkey_name
        self._listener = None
        self._is_recording = False
        self._stop_requested = False
        self._last_event_time = None
        self.countdown_duration = 3

    def _start_actual_recording(self):
        self._is_recording = True
        self._last_event_time = time.perf_counter()
        self.recording_status_update.emit(Translations.get("status_recorder_recording", hotkey_name=self.stop_record_hotkey_name))

        def on_press(key):
            if not self._is_recording or self._stop_requested: return False
            current_time = time.perf_counter()
            delay_ms = (current_time - self._last_event_time) * 1000 if self._last_event_time else 0
            self._last_event_time = current_time
            key_name = get_pynput_key_display_name(key)
            actual_key_obj = key # Luu KeyCode hoac Key enum
            self.key_event_recorded.emit(actual_key_obj, key_name, "press", delay_ms) # action_canonical
            return not self._stop_requested

        def on_release(key):
            if not self._is_recording or self._stop_requested: return False
            current_time = time.perf_counter()
            delay_ms = (current_time - self._last_event_time) * 1000
            self._last_event_time = current_time
            key_name = get_pynput_key_display_name(key)
            actual_key_obj = key
            self.key_event_recorded.emit(actual_key_obj, key_name, "release", delay_ms) # action_canonical
            if self._stop_requested : return False
            return not self._stop_requested

        try:
            # suppress=True de tranh ghi thao tac vao ung dung khac khi dang record (co the tuy chinh)
            self._listener = PynputListener(on_press=on_press, on_release=on_release, suppress=False)
            self._listener.start()
            self._listener.join()
        except Exception:
            # Log loi o day neu can
            pass
        finally:
            self._is_recording = False
            self.recording_finished.emit() # Dam bao emit ngay ca khi co loi listener

    @Slot()
    def run(self):
        for i in range(self.countdown_duration, 0, -1):
            if self._stop_requested:
                self.recording_finished.emit()
                return
            self.recording_status_update.emit(Translations.get("status_recorder_countdown", seconds=i))
            time.sleep(1)

        if self._stop_requested: # Check lai sau khi dem nguoc
            self.recording_finished.emit()
            return
        self._start_actual_recording()

    @Slot()
    def request_stop(self):
        self._stop_requested = True
        if self._listener and self._listener.is_alive():
            try:
                self._listener.stop()
            except Exception:
                pass


# --- Worker phát lại thao tác bàn phím ---
class RecordedPlayerWorker(QObject):
    update_status_signal = Signal(str)
    playing_finished_signal = Signal()
    error_signal = Signal(str)

    # recorded_events la list cua (key_obj, action_canonical, delay_ms)
    def __init__(self, recorded_events, repetitions, play_stop_hotkey_name): # Them repetitions
        super().__init__()
        self.recorded_events = recorded_events
        self.repetitions = repetitions # Luu so lan lap
        self.play_stop_hotkey_name = play_stop_hotkey_name
        self.keyboard_controller = PynputController()
        self._is_running_request = True
        self.total_actions_per_rep = len(recorded_events) # So hanh dong trong 1 lan lap

    @Slot()
    def run(self):
        error_emitted = False # Flag theo doi loi
        try:
            if not self.recorded_events:
                self.error_signal.emit(Translations.get("msgbox_no_recording_text"))
                error_emitted = True
                return
            if self.repetitions < 0: # So lan lap khong hop le
                # Co the them mot translation key moi cho loi nay neu can
                self.error_signal.emit(Translations.get("worker_invalid_repetitions_error"))
                error_emitted = True
                return

            initial_delay = 0.5 # Cho phep nguoi dung tha hotkey
            start_time = time.perf_counter()
            while time.perf_counter() - start_time < initial_delay:
                if not self._is_running_request:
                    return # Finally se emit finished
                time.sleep(0.05)

            current_rep = 0
            while self._is_running_request:
                if self.repetitions != 0 and current_rep >= self.repetitions:
                    break # Da hoan thanh so lan lap yeu cau

                rep_total_display_text = str(self.repetitions) if self.repetitions != 0 else Translations.get("rep_text_infinite")

                for i, (key_obj, action_canonical, delay_ms) in enumerate(self.recorded_events):
                    if not self._is_running_request: break

                    if delay_ms > 0:
                        sleep_start_time = time.perf_counter()
                        target_sleep_s = delay_ms / 1000.0
                        while time.perf_counter() - sleep_start_time < target_sleep_s:
                            if not self._is_running_request: break
                            remaining_sleep_s = target_sleep_s - (time.perf_counter() - sleep_start_time)
                            time.sleep(max(0, min(0.01, remaining_sleep_s)))
                    if not self._is_running_request: break

                    if action_canonical == "press":
                        self.keyboard_controller.press(key_obj)
                    elif action_canonical == "release":
                        self.keyboard_controller.release(key_obj)

                    self.update_status_signal.emit(
                        Translations.get("status_player_playing",
                                         rep_count=current_rep + 1,
                                         rep_total_text=rep_total_display_text,
                                         current_action=i + 1,
                                         total_actions=self.total_actions_per_rep,
                                         hotkey_name=self.play_stop_hotkey_name)
                    )
                
                if not self._is_running_request: # Kiem tra sau vong lap action
                    break
                current_rep += 1

        except Exception as e:
            self.error_signal.emit(Translations.get("worker_runtime_error", error_message=str(e)))
            error_emitted = True
        finally:
            if not error_emitted:
                self.playing_finished_signal.emit()

    @Slot()
    def request_stop(self):
        self._is_running_request = False