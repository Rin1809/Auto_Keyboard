# core/translations.py

class Translations:
    LANG_VI = "vi"
    LANG_EN = "en"
    LANG_JA = "ja"

    lang_map = { # Map code voi ten hien thi
        LANG_VI: "Tiếng Việt",
        LANG_EN: "English",
        LANG_JA: "日本語"
    }

    translations = {
        "window_title": {
            LANG_VI: "AutoTyper",
            LANG_EN: "AutoTyper",
            LANG_JA: "AutoTyper"
        },
        "title_bar_text": { # hotkey
            LANG_VI: "AutoTyper - Hotkey: {hotkey}",
            LANG_EN: "AutoTyper - Hotkey: {hotkey}",
            LANG_JA: "AutoTyper - ホットキー: {hotkey}"
        },
        "error_loading_background_msg_console": { # path
            LANG_VI: "Loi: Khong the tai anh nen tu '{path}'",
            LANG_EN: "Error: Could not load background image from '{path}'",
            LANG_JA: "エラー: 背景画像を '{path}' から読み込めませんでした"
        },
        "error_loading_background_ui": {
            LANG_VI: "Lỗi tải ảnh nền! Kiểm tra console.",
            LANG_EN: "Background image load error! Check console.",
            LANG_JA: "背景画像の読み込みエラー！コンソールを確認してください。"
        },
        "worker_empty_text_error": {
            LANG_VI: "Vui lòng nhập văn bản/phím cần nhấn.",
            LANG_EN: "Please enter text/keys to press.",
            LANG_JA: "入力するテキスト/キーを入力してください。"
        },
        "worker_invalid_interval_error": {
            LANG_VI: "Khoảng thời gian phải lớn hơn 0.",
            LANG_EN: "Interval must be greater than 0.",
            LANG_JA: "間隔は0より大きくする必要があります。"
        },
        "worker_invalid_repetitions_error": {
            LANG_VI: "Số lần lặp lại phải là số không âm.",
            LANG_EN: "Repetitions must be a non-negative number.",
            LANG_JA: "繰り返し回数は負でない数である必要があります。"
        },
        "worker_status_running": { # count, rep_text, hotkey_display_name
            LANG_VI: "Đang chạy... (Lần {count}/{rep_text}). Nhấn {hotkey_display_name} để dừng.",
            LANG_EN: "Running... (Count {count}/{rep_text}). Press {hotkey_display_name} to stop.",
            LANG_JA: "実行中... (回数 {count}/{rep_text})。{hotkey_display_name} を押して停止。"
        },
        "worker_runtime_error": { # error_message
            LANG_VI: "Lỗi trong quá trình chạy: {error_message}",
            LANG_EN: "Error during execution: {error_message}",
            LANG_JA: "実行中のエラー: {error_message}"
        },
        "text_input_placeholder": {
            LANG_VI: "Nhập văn bản hoặc <key_name>...",
            LANG_EN: "Enter text or <key_name>...",
            LANG_JA: "テキストまたは <key_name> を入力..."
        },
        "label_text_key": {
            LANG_VI: "Văn bản/Phím:",
            LANG_EN: "Text/Key:",
            LANG_JA: "テキスト/キー:"
        },
        "label_interval": {
            LANG_VI: "Khoảng thời gian:",
            LANG_EN: "Interval:",
            LANG_JA: "間隔:"
        },
        "interval_suffix": {
            LANG_VI: " ms",
            LANG_EN: " ms",
            LANG_JA: "ミリ秒"
        },
        "label_repetitions": {
            LANG_VI: "Số lần lặp:",
            LANG_EN: "Repetitions:",
            LANG_JA: "繰り返し回数:"
        },
        "repetitions_infinite": {
            LANG_VI: "Vô hạn (0)",
            LANG_EN: "Infinite (0)",
            LANG_JA: "無限 (0)"
        },
        "button_start": { # hotkey_name
            LANG_VI: "Start ({hotkey_name})",
            LANG_EN: "Start ({hotkey_name})",
            LANG_JA: "開始 ({hotkey_name})"
        },
        "button_stop": {
            LANG_VI: "Stop",
            LANG_EN: "Stop",
            LANG_JA: "停止"
        },
        "status_ready": { # hotkey_name
            LANG_VI: "Sẵn sàng. Nhấn '{hotkey_name}' để bắt đầu.",
            LANG_EN: "Ready. Press '{hotkey_name}' to start.",
            LANG_JA: "準備完了。'{hotkey_name}' を押して開始。"
        },
        "msgbox_missing_info_title": {
            LANG_VI: "Thiếu thông tin",
            LANG_EN: "Missing Information",
            LANG_JA: "情報不足"
        },
        "button_start_loading": {
            LANG_VI: "...",
            LANG_EN: "...",
            LANG_JA: "..."
        },
        "status_preparing": { # hotkey_name
            LANG_VI: "Chuẩn bị... (Nhấn '{hotkey_name}' để dừng)",
            LANG_EN: "Preparing... (Press '{hotkey_name}' to stop)",
            LANG_JA: "準備中... ('{hotkey_name}' を押して停止)"
        },
        "status_requesting_stop": {
            LANG_VI: "Đang yêu cầu dừng...",
            LANG_EN: "Requesting stop...",
            LANG_JA: "停止を要求中..."
        },
        "msgbox_autotyper_error_title": {
            LANG_VI: "Lỗi AutoTyper/Player", # Thay doi de dung chung
            LANG_EN: "AutoTyper/Player Error",
            LANG_JA: "AutoTyper/Player エラー"
        },
        "status_stopped": { # hotkey_name
            LANG_VI: "Đã dừng. Nhấn '{hotkey_name}' để bắt đầu.",
            LANG_EN: "Stopped. Press '{hotkey_name}' to start.",
            LANG_JA: "停止しました。'{hotkey_name}' を押して開始。"
        },
        "status_stopped_fully": { # hotkey_name
            LANG_VI: "Đã dừng (hoàn toàn). Nhấn '{hotkey_name}' để bắt đầu.",
            LANG_EN: "Stopped (fully). Press '{hotkey_name}' to start.",
            LANG_JA: "停止しました (完全に)。'{hotkey_name}' を押して開始。"
        },
        "custom_title_bar_default_title": {
            LANG_VI: "AutoTyper Poetic",
            LANG_EN: "AutoTyper Poetic",
            LANG_JA: "AutoTyper Poetic"
        },
         "rep_text_infinite": {
            LANG_VI: "∞",
            LANG_EN: "∞",
            LANG_JA: "∞"
        },
        "label_hotkey_setting_group": {
            LANG_VI: "Cài đặt Hotkey",
            LANG_EN: "Hotkey Settings",
            LANG_JA: "ホットキー設定"
        },
        "label_current_hotkey": {
            LANG_VI: "Hotkey hiện tại:",
            LANG_EN: "Current Hotkey:",
            LANG_JA: "現在のホットキー:"
        },
        "button_set_hotkey": {
            LANG_VI: "Thay đổi Hotkey",
            LANG_EN: "Change Hotkey",
            LANG_JA: "ホットキー変更"
        },
        "button_setting_hotkey_wait": {
            LANG_VI: "Nhấn phím mới...",
            LANG_EN: "Press new key...",
            LANG_JA: "新しいキーを押してください..."
        },
        "msgbox_hotkey_set_title": {
            LANG_VI: "Hotkey đã được đặt",
            LANG_EN: "Hotkey Set",
            LANG_JA: "ホットキー設定完了"
        },
        "msgbox_hotkey_set_text": { # new_hotkey_name
            LANG_VI: "Hotkey mới: {new_hotkey_name}",
            LANG_EN: "New hotkey: {new_hotkey_name}",
            LANG_JA: "新しいホットキー: {new_hotkey_name}"
        },
        "msgbox_error_set_hotkey_title": {
            LANG_VI: "Lỗi đặt Hotkey",
            LANG_EN: "Hotkey Set Error",
            LANG_JA: "ホットキー設定エラー"
        },
        "msgbox_error_set_hotkey_text": { # error_message
            LANG_VI: "Không thể đặt hotkey: {error_message}",
            LANG_EN: "Could not set hotkey: {error_message}",
            LANG_JA: "ホットキーを設定できませんでした: {error_message}"
        },
        "action_description_autotyper": { # Mo ta chuc nang auto typer
            LANG_VI: "AutoTyper chính",
            LANG_EN: "Main AutoTyper",
            LANG_JA: "メインオートタイパー"
        },
        "action_description_record": { # Mo ta chuc nang ghi
            LANG_VI: "Ghi thao tác",
            LANG_EN: "Record actions",
            LANG_JA: "操作の記録"
        },
        "action_description_play": { # Mo ta chuc nang phat
            LANG_VI: "Phát thao tác",
            LANG_EN: "Play actions",
            LANG_JA: "操作の再生"
        },
        "msgbox_hotkey_conflict_title": { # Tieu de khi hotkey trung
            LANG_VI: "Xung đột Hotkey",
            LANG_EN: "Hotkey Conflict",
            LANG_JA: "ホットキーの競合"
        },
        "msgbox_hotkey_conflict_text": { # Noi dung khi hotkey trung
            LANG_VI: "Hotkey '{new_hotkey_name}' đã được sử dụng cho '{action_description}'. Vui lòng chọn phím khác.",
            LANG_EN: "Hotkey '{new_hotkey_name}' is already in use for '{action_description}'. Please choose a different key.",
            LANG_JA: "ホットキー '{new_hotkey_name}' は既に '{action_description}' で使用されています。別のキーを選択してください。"
        },
        # --- Record Feature Translations ---
        "button_advanced_mode": {
            LANG_VI: "Nâng cao",
            LANG_EN: "Advanced",
            LANG_JA: "高度な設定"
        },
        "button_autotyper_mode": {
            LANG_VI: "AutoTyper",
            LANG_EN: "AutoTyper",
            LANG_JA: "オートタイパー"
        },
        "label_record_play_group": {
            LANG_VI: "Ghi & Phát Thao Tác",
            LANG_EN: "Record & Play Actions",
            LANG_JA: "操作の記録と再生"
        },
        "label_start_record_hotkey": {
            LANG_VI: "Hotkey Ghi/Dừng:",
            LANG_EN: "Record/Stop Hotkey:",
            LANG_JA: "録画/停止ホットキー:"
        },
        "button_set_start_record_hotkey": {
            LANG_VI: "Đổi Hotkey Ghi",
            LANG_EN: "Change Rec. Hotkey",
            LANG_JA: "録画ホットキー変更"
        },
        "label_play_record_hotkey": {
            LANG_VI: "Hotkey Phát/Dừng:",
            LANG_EN: "Play/Stop Hotkey:",
            LANG_JA: "再生/停止ホットキー:"
        },
        "button_set_play_record_hotkey": {
            LANG_VI: "Đổi Hotkey Phát",
            LANG_EN: "Change Play Hotkey",
            LANG_JA: "再生ホットキー変更"
        },
        "button_start_recording": { # hotkey_name
            LANG_VI: "Bắt đầu Ghi ({hotkey_name})",
            LANG_EN: "Start Recording ({hotkey_name})",
            LANG_JA: "録画開始 ({hotkey_name})"
        },
        "button_stop_recording": { # hotkey_name
            LANG_VI: "Dừng Ghi ({hotkey_name})",
            LANG_EN: "Stop Recording ({hotkey_name})",
            LANG_JA: "録画停止 ({hotkey_name})"
        },
        "button_play_recording": { # hotkey_name
            LANG_VI: "Phát Bản Ghi ({hotkey_name})",
            LANG_EN: "Play Recording ({hotkey_name})",
            LANG_JA: "再生 ({hotkey_name})"
        },
         "button_stop_playing_recording": { # hotkey_name
            LANG_VI: "Dừng Phát ({hotkey_name})",
            LANG_EN: "Stop Playing ({hotkey_name})",
            LANG_JA: "再生停止 ({hotkey_name})"
        },
        "button_clear_recording": {
            LANG_VI: "Xóa Bản Ghi",
            LANG_EN: "Clear Recording",
            LANG_JA: "録画を消去"
        },
        "status_recorder_idle": { # hotkey_name
            LANG_VI: "Sẵn sàng. Nhấn '{hotkey_name}' để ghi.",
            LANG_EN: "Ready. Press '{hotkey_name}' to record.",
            LANG_JA: "準備完了。'{hotkey_name}' を押して録画開始。"
        },
        "status_recorder_countdown": { # seconds
            LANG_VI: "Bắt đầu ghi sau: {seconds}...",
            LANG_EN: "Starting recording in: {seconds}...",
            LANG_JA: "録画開始まで: {seconds}..."
        },
        "status_recorder_recording": { # hotkey_name
            LANG_VI: "Đang ghi... Nhấn '{hotkey_name}' để dừng.",
            LANG_EN: "Recording... Press '{hotkey_name}' to stop.",
            LANG_JA: "録画中... '{hotkey_name}' を押して停止。"
        },
        "status_recorder_stopped": { # hotkey_name
            LANG_VI: "Đã dừng ghi. Nhấn '{hotkey_name}' để ghi lại.",
            LANG_EN: "Recording stopped. Press '{hotkey_name}' to record again.",
            LANG_JA: "録画停止。'{hotkey_name}' を押して再録画。"
        },
        "status_player_playing": { # rep_count, rep_total_text, current_action, total_actions, hotkey_name
            LANG_VI: "Đang phát... (Lặp {rep_count}/{rep_total_text}, HĐ {current_action}/{total_actions}). Nhấn '{hotkey_name}' để dừng.",
            LANG_EN: "Playing... (Rep {rep_count}/{rep_total_text}, Act {current_action}/{total_actions}). Press '{hotkey_name}' to stop.",
            LANG_JA: "再生中... (反復 {rep_count}/{rep_total_text}、動作 {current_action}/{total_actions})。'{hotkey_name}' を押して停止。"
        },
        "status_player_stopped": { # hotkey_name
            LANG_VI: "Đã dừng phát. Nhấn '{hotkey_name}' để phát lại.",
            LANG_EN: "Playback stopped. Press '{hotkey_name}' to play again.",
            LANG_JA: "再生停止。'{hotkey_name}' を押して再再生。"
        },
        "status_player_error": { # hotkey_name. Them moi
            LANG_VI: "Lỗi phát lại! Nhấn '{hotkey_name}' để thử lại.",
            LANG_EN: "Playback error! Press '{hotkey_name}' to retry.",
            LANG_JA: "再生エラー！'{hotkey_name}' を押して再試行してください。"
        },
        "status_player_ready": { # hotkey_name
            LANG_VI: "Sẵn sàng phát. Nhấn '{hotkey_name}' để phát.",
            LANG_EN: "Ready to play. Press '{hotkey_name}' to play.",
            LANG_JA: "再生準備完了。'{hotkey_name}' を押して再生。"
        },
        "table_header_key": {
            LANG_VI: "Phím",
            LANG_EN: "Key",
            LANG_JA: "キー"
        },
        "table_header_action": {
            LANG_VI: "Hành động",
            LANG_EN: "Action",
            LANG_JA: "アクション"
        },
        "table_header_delay": {
            LANG_VI: "Trễ (ms)",
            LANG_EN: "Delay (ms)",
            LANG_JA: "遅延 (ミリ秒)"
        },
        "action_press": { # Dung boi worker cu, se duoc thay the
            LANG_VI: "Nhấn",
            LANG_EN: "Press",
            LANG_JA: "押す"
        },
        "action_release": { # Dung boi worker cu, se duoc thay the
            LANG_VI: "Thả",
            LANG_EN: "Release",
            LANG_JA: "離す"
        },
        "action_press_display": { # Cho table display, canonical la "press"
            LANG_VI: "Nhấn",
            LANG_EN: "Press",
            LANG_JA: "押す"
        },
        "action_release_display": { # Cho table display, canonical la "release"
            LANG_VI: "Thả",
            LANG_EN: "Release",
            LANG_JA: "離す"
        },
        "msgbox_no_recording_title": {
            LANG_VI: "Không có Bản ghi",
            LANG_EN: "No Recording",
            LANG_JA: "記録なし"
        },
        "msgbox_no_recording_text": {
            LANG_VI: "Chưa có thao tác nào được ghi lại để phát.",
            LANG_EN: "No actions have been recorded to play.",
            LANG_JA: "再生する記録された操作はありません。"
        },
        "msgbox_confirm_clear_recording_title": {
            LANG_VI: "Xác nhận Xóa",
            LANG_EN: "Confirm Clear",
            LANG_JA: "クリアの確認"
        },
        "msgbox_confirm_clear_recording_text": {
            LANG_VI: "Bạn có chắc muốn xóa toàn bộ bản ghi hiện tại không?",
            LANG_EN: "Are you sure you want to clear the current recording?",
            LANG_JA: "現在の記録をすべてクリアしてもよろしいですか？"
        },
        "recorder_status_label_default": {
            LANG_VI: "Trạng thái ghi/phát.",
            LANG_EN: "Recorder/Player status.",
            LANG_JA: "録画/再生ステータス。"
        },
        # --- Config save/load messages (for console logging) ---
        "config_file_not_found": { # filepath
            LANG_VI: "INFO: Không tìm thấy file cài đặt ({filepath}). Sử dụng cài đặt mặc định.",
            LANG_EN: "INFO: Settings file not found ({filepath}). Using default settings.",
            LANG_JA: "INFO: 設定ファイルが見つかりません ({filepath})。デフォルト設定を使用します。"
        },
        "config_loaded_error": { # filepath, error
            LANG_VI: "WARNING: Lỗi khi tải cài đặt từ '{filepath}': {error}. Sử dụng cài đặt mặc định.",
            LANG_EN: "WARNING: Error loading settings from '{filepath}': {error}. Using default settings.",
            LANG_JA: "WARNING: '{filepath}' から設定を読み込む際にエラーが発生しました: {error}。デフォルト設定を使用します。"
        },
        "config_saved_error": { # filepath, error
            LANG_VI: "ERROR: Lỗi khi lưu cài đặt vào '{filepath}': {error}",
            LANG_EN: "ERROR: Error saving settings to '{filepath}': {error}",
            LANG_JA: "ERROR: '{filepath}' への設定保存中にエラーが発生しました: {error}"
        },
        # --- New config buttons and messages ---
        "button_load_config": {
            LANG_VI: "Tải Cấu hình",
            LANG_EN: "Load Config",
            LANG_JA: "設定読込"
        },
        "button_save_config_as": { # "Luu cau hinh" -> "Luu thanh file moi"
            LANG_VI: "Lưu dạng...",
            LANG_EN: "Save As...",
            LANG_JA: "名前を付けて保存..."
        },
        "button_save_current_config": {
            LANG_VI: "Lưu Hiện tại",
            LANG_EN: "Save Current",
            LANG_JA: "現設定保存"
        },
        "msgbox_load_config_title": {
            LANG_VI: "Tải Cấu hình",
            LANG_EN: "Load Configuration",
            LANG_JA: "設定の読み込み"
        },
        "msgbox_save_config_as_title": {
            LANG_VI: "Lưu Cấu hình Dạng...",
            LANG_EN: "Save Configuration As...",
            LANG_JA: "名前を付けて設定を保存"
        },
         "msgbox_save_current_config_title": {
            LANG_VI: "Lưu Cấu hình Hiện tại",
            LANG_EN: "Save Current Configuration",
            LANG_JA: "現在の設定を保存"
        },
        "msgbox_load_success_title": {
            LANG_VI: "Tải Thành công",
            LANG_EN: "Load Successful",
            LANG_JA: "読み込み成功"
        },
        "msgbox_load_success_text": { # filename
            LANG_VI: "Cấu hình '{filename}' đã được tải thành công.",
            LANG_EN: "Configuration '{filename}' loaded successfully.",
            LANG_JA: "設定 '{filename}' が正常に読み込まれました。"
        },
        "msgbox_load_fail_title": {
            LANG_VI: "Tải Thất bại",
            LANG_EN: "Load Failed",
            LANG_JA: "読み込み失敗"
        },
        "msgbox_load_fail_text": { # filename, error
            LANG_VI: "Không thể tải cấu hình từ '{filename}': {error}",
            LANG_EN: "Could not load configuration from '{filename}': {error}",
            LANG_JA: "設定を '{filename}' から読み込めませんでした: {error}"
        },
        "msgbox_save_success_title": {
            LANG_VI: "Lưu Thành công",
            LANG_EN: "Save Successful",
            LANG_JA: "保存成功"
        },
        "msgbox_save_success_text": { # filename
            LANG_VI: "Cấu hình đã được lưu thành công vào '{filename}'.",
            LANG_EN: "Configuration saved successfully to '{filename}'.",
            LANG_JA: "設定が '{filename}' に正常に保存されました。"
        },
        "msgbox_save_fail_title": {
            LANG_VI: "Lưu Thất bại",
            LANG_EN: "Save Failed",
            LANG_JA: "保存失敗"
        },
        "msgbox_save_fail_text": { # filename, error
            LANG_VI: "Không thể lưu cấu hình vào '{filename}': {error}",
            LANG_EN: "Could not save configuration to '{filename}': {error}",
            LANG_JA: "設定を '{filename}' に保存できませんでした: {error}"
        },
        "file_dialog_json_filter": {
            LANG_VI: "Tệp JSON (*.json)",
            LANG_EN: "JSON Files (*.json)",
            LANG_JA: "JSONファイル (*.json)"
        }
    }
    current_lang = LANG_VI

    @classmethod
    def set_language(cls, lang_code): # Dat ngon ngu
        if lang_code in [cls.LANG_VI, cls.LANG_EN, cls.LANG_JA]:
            cls.current_lang = lang_code
        else: # Mac dinh tieng Viet neu ko ho tro
            print(f"Unsupported language: {lang_code}. Defaulting to {cls.LANG_VI}")
            cls.current_lang = cls.LANG_VI

    @classmethod
    def get(cls, key, **kwargs): # Lay chuoi dich
        try:
            translation_dict = cls.translations[key]
            # Uu tien ngon ngu hien tai, sau do la tieng Anh, cuoi cung la khoa
            raw_translation = translation_dict.get(cls.current_lang, translation_dict.get(cls.LANG_EN, key))
            return raw_translation.format(**kwargs) if kwargs else raw_translation
        except KeyError:
       
            return key