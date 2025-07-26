

# AutoTyper - Advanced Keyboard Automation ᓚᘏᗢ

## Demo

-   **AutoTyper Mode:**

![AutoTyper Demo](https://github.com/user-attachments/assets/ef176550-8ded-4f61-844e-f032655f10b5)

---
-   **Keyboard Recorder & Player Mode:**

![Keyboard Recorder Demo](https://github.com/user-attachments/assets/360559af-eb63-4160-b7d7-c50bbb783c36)

---
## DOCS:

<!-- Vietnamese -->
<details>
<summary>🇻🇳 Tiếng Việt (Chi tiết)</summary>

## Tổng quan

**AutoTyper Poetic** là một ứng dụng máy tính để bàn được thiết kế để tự động hóa các tác vụ nhập liệu bàn phím. Ứng dụng cung cấp hai chế độ chính:
1.  **Chế độ AutoTyper:** Cho phép gõ văn bản hoặc phím cụ thể một cách lặp đi lặp lại.
2.  **Chế độ Ghi & Phát:** Cho phép ghi lại các chuỗi hành động bàn phím phức tạp và phát lại chúng một cách chính xác.

Với giao diện người dùng thân thiện được xây dựng bằng Python và PySide6, cùng với thư viện `pynput` để xử lý tương tác bàn phím, AutoTyper Poetic mang đến trải nghiệm mượt mà và hiệu quả.

## Lưu ý quan trọng

*   📜 **Tệp cấu hình:** Mọi cài đặt của người dùng (ngôn ngữ, kích thước cửa sổ, hotkey, các macro đã ghi, v.v.) được lưu trữ trong tệp `autokeyboard_config.json` tại thư mục gốc của ứng dụng. Điều này đảm bảo các tùy chỉnh của bạn được giữ lại sau mỗi lần sử dụng.
*   🚀 **Thiết lập tự động:** Các tệp `run.bat` (cho Windows) và `run.sh` (cho Linux/macOS) được cung cấp để tự động hóa quá trình tạo môi trường ảo (nếu chưa có) và cài đặt các thư viện cần thiết, giúp bạn khởi chạy ứng dụng một cách nhanh chóng.

## Tính năng nổi bật

*   **Hoạt động Hai Chế độ Linh hoạt:**
    *   **Chế độ AutoTyper (Cơ bản):**
        *   Tự động gõ văn bản do người dùng xác định hoặc các phím đặc biệt (ví dụ: `<enter>`, `<f1>`, `<space>`).
        *   Khoảng thời gian giữa các lần gõ có thể điều chỉnh (đơn vị: mili giây).
        *   Số lần lặp lại có thể cấu hình (nhập `0` cho vô hạn).
        *   Hotkey chuyên dụng (mặc định là **F9**, có thể thay đổi) để bắt đầu/dừng việc gõ tự động.
    *   **Chế độ Ghi & Phát (Nâng cao):**
        *   Ghi lại chuỗi các hành động bàn phím (nhấn phím, thả phím) cùng với độ trễ chính xác giữa chúng.
        *   Lớp phủ đếm ngược trực quan (3 giây) trước khi bắt đầu ghi, giúp bạn chuẩn bị.
        *   Các hotkey chuyên dụng (mặc định **F10** để Ghi/Dừng Ghi, **F11** để Phát/Dừng Phát, có thể thay đổi).
        *   Các hành động đã ghi được hiển thị rõ ràng trong bảng (Phím, Hành động, Độ trễ).
        *   Phát lại các chuỗi đã ghi với số lần lặp có thể điều chỉnh (nhập `0` cho vô hạn).
        *   Tùy chọn **Xóa Bản Ghi** để loại bỏ các hành động đã lưu.
*   **Giao diện Người dùng Trực quan & Thân thiện:**
    *   Thiết kế hiện đại, dễ sử dụng với PySide6.
    *   Thanh tiêu đề tùy chỉnh với các nút điều khiển cửa sổ tiêu chuẩn (thu nhỏ, phóng to, đóng) và giao diện được tùy biến.
    *   Hỗ trợ kéo thả và thay đổi kích thước cửa sổ linh hoạt.
    *   Hiệu ứng chuyển động mượt mà khi mở/đóng cửa sổ và chuyển đổi giữa các chế độ.
*   **Hỗ trợ Đa ngôn ngữ:**
    *   Giao diện có sẵn bằng Tiếng Anh (English), Tiếng Việt (Vietnamese), và Tiếng Nhật (日本語).
    *   Dễ dàng chuyển đổi ngôn ngữ thông qua menu thả xuống trên thanh tiêu đề.
*   **Quản lý Cấu hình Nâng cao:**
    *   Tất cả cài đặt được lưu trữ bền vững trong tệp `autokeyboard_config.json`.
    *   Lưu trữ tùy chọn ngôn ngữ, kích thước/vị trí cửa sổ, chế độ hoạt động (AutoTyper/Nâng cao), tất cả các hotkey, cài đặt của AutoTyper, và các macro đã ghi.
    *   Các chức năng tiện ích: **Tải Cấu hình** (từ tệp `.json` bất kỳ), **Lưu dạng...** (lưu cấu hình hiện tại ra tệp `.json` mới), và **Lưu Hiện tại** (lưu vào tệp cấu hình đang sử dụng).
*   **Quản lý Hotkey Thông minh:**
    *   Giao diện dễ sử dụng để thay đổi hotkey cho AutoTyper, Bắt đầu/Dừng Ghi, và Bắt đầu/Dừng Phát lại.
    *   Tự động phát hiện xung đột hotkey để tránh gán cùng một phím cho nhiều hành động, đảm bảo hoạt động ổn định.
*   **Tương thích Đa nền tảng:**
    *   Cung cấp `run.bat` cho Windows và `run.sh` cho Linux/macOS để đơn giản hóa việc thiết lập và thực thi.
    *   Các script này tự động xử lý việc tạo môi trường ảo và cài đặt các thư viện phụ thuộc.
*   **Phản hồi Trạng thái Rõ ràng:**
    *   Cập nhật trạng thái theo thời gian thực ngay trên giao diện ứng dụng.
    *   Lớp phủ đếm ngược trực quan khi chuẩn bị ghi.
    *   Các hộp thoại thông báo lỗi và xác nhận chi tiết, giúp người dùng dễ dàng theo dõi và xử lý.

## Điều kiện tiên quyết (Để chạy từ mã nguồn)

1.  **Python:** Khuyến nghị sử dụng Python 3.x. Các script `run.bat`/`run.sh` sẽ cố gắng sử dụng `python` (Windows) hoặc `python3`/`python` (Linux/macOS) có sẵn trong PATH hệ thống.
2.  **Pip:** Trình quản lý gói Python (thường được cài đặt sẵn cùng với Python).

## Cài đặt & Chạy ứng dụng (Từ mã nguồn)

Cách dễ nhất và được khuyến nghị để chạy ứng dụng là sử dụng các script tự động hóa được cung cấp:

### Sử dụng Script (Khuyến nghị)

1.  **Tải mã nguồn:**
    *   Sao chép (clone) repository này hoặc tải về dưới dạng tệp ZIP và giải nén.

2.  **Chạy script cài đặt và khởi động:**
    *   **Trên Windows:**
        1.  Điều hướng đến thư mục `windows` trong thư mục gốc của dự án.
        2.  Nhấp đúp để chạy tệp `run.bat`.
    *   **Trên Linux/macOS:**
        1.  Mở Terminal.
        2.  Điều hướng đến thư mục `linux-mac` trong thư mục gốc của dự án.
        3.  Cấp quyền thực thi cho script: `chmod +x run.sh`
        4.  Chạy script: `./run.sh`

    Các script này sẽ tự động thực hiện các bước sau:
    *   Kiểm tra và tạo một môi trường ảo Python có tên là `venv` trong thư mục gốc của dự án (nếu nó chưa tồn tại).
    *   Kích hoạt môi trường ảo.
    *   Cài đặt tất cả các thư viện cần thiết từ tệp `requirements.txt`.
    *   Khởi chạy ứng dụng AutoTyper Poetic.

### Cài đặt Thủ công (Tùy chọn nâng cao)

Nếu bạn muốn kiểm soát quá trình cài đặt một cách chi tiết hơn:

1.  **Tải mã nguồn** (như trên).
2.  Mở Terminal hoặc Command Prompt, điều hướng đến thư mục gốc của dự án.
3.  **(Khuyến nghị)** Tạo và kích hoạt một môi trường ảo Python:
    ```bash
    python -m venv venv
    ```
    *   Trên Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   Trên Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
4.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```
5.  Chạy ứng dụng:
    ```bash
    python main.py
    ```

## Hướng dẫn sử dụng

Sau khi ứng dụng đã khởi chạy:

### Thiết lập Chung

*   **Chuyển đổi Chế độ:** Sử dụng nút **"Nâng cao"** / **"AutoTyper"** trên thanh tiêu đề để chuyển đổi giữa chế độ AutoTyper cơ bản và chế độ Ghi & Phát nâng cao.
*   **Chọn Ngôn ngữ:** Sử dụng menu thả xuống ngôn ngữ (ví dụ: "Tiếng Việt", "English", "日本語") trên thanh tiêu đề.

### Chế độ AutoTyper

1.  **Văn bản/Phím:** Nhập văn bản bạn muốn gõ tự động. Đối với các phím đặc biệt, sử dụng định dạng `<key_name>` (ví dụ: `<enter>`, `<f12>`, `<space>`, `<ctrl>`, `<alt>`, `<shift>`).
2.  **Khoảng thời gian:** Đặt khoảng thời gian (tính bằng mili giây) giữa mỗi lần gõ hoặc nhấn phím.
3.  **Số lần lặp:** Đặt số lần lặp lại (nhập `0` để lặp vô hạn).
4.  **Hotkey AutoTyper:**
    *   Mặc định là **F9**.
    *   Nhấn nút **"Thay đổi Hotkey"** để đặt một hotkey mới. Một thông báo sẽ yêu cầu bạn nhấn phím mong muốn.
    *   Nhấn hotkey này để **Bắt đầu** hoặc **Dừng** quá trình gõ tự động.
5.  **Nút Start/Stop:**
    *   Nhấn nút **"Start (Tên_Hotkey)"** để bắt đầu.
    *   Khi đang chạy, nút này sẽ chuyển thành **"..."** (đang tải) và nút **"Stop"** sẽ được kích hoạt để bạn dừng lại.

### Chế độ Ghi & Phát (Nâng cao)

1.  **Cài đặt Hotkey:**
    *   **Hotkey Ghi/Dừng:** Mặc định là **F10**. Dùng để bắt đầu (sau khi đếm ngược 3 giây) và dừng quá trình ghi. Thay đổi bằng nút **"Đổi Hotkey Ghi"**.
    *   **Hotkey Phát/Dừng:** Mặc định là **F11**. Dùng để bắt đầu và dừng phát lại các hành động đã ghi. Thay đổi bằng nút **"Đổi Hotkey Phát"**.
2.  **Số lần lặp (Phát lại):** Đặt số lần bạn muốn chuỗi hành động được phát lại (nhập `0` cho vô hạn).
3.  **Quá trình Ghi:**
    *   Nhấn nút **"Bắt đầu Ghi (Tên_Hotkey_Ghi)"** hoặc nhấn hotkey ghi.
    *   Một lớp phủ đếm ngược sẽ xuất hiện. Sau khi đếm ngược kết thúc, mọi thao tác nhấn/thả phím của bạn sẽ được ghi lại.
    *   Nhấn nút **"Dừng Ghi (Tên_Hotkey_Ghi)"** hoặc nhấn lại hotkey ghi để kết thúc.
4.  **Quá trình Phát lại:**
    *   Sau khi đã có bản ghi, nhấn nút **"Phát Bản Ghi (Tên_Hotkey_Phát)"** hoặc nhấn hotkey phát.
    *   Để dừng, nhấn nút **"Dừng Phát (Tên_Hotkey_Phát)"** hoặc nhấn lại hotkey phát.
5.  **Xóa Bản Ghi:** Nhấn nút **"Xóa Bản Ghi"** để xóa tất cả các hành động đã được ghi trong bảng. Một hộp thoại xác nhận sẽ xuất hiện.
6.  **Bảng sự kiện:** Hiển thị chi tiết các phím đã ghi, hành động (Nhấn/Thả) và độ trễ (ms) giữa các hành động.

### Quản lý Cấu hình

Các nút quản lý cấu hình nằm trên thanh tiêu đề:

*   **Tải Cấu hình:** Nhấn nút này (biểu tượng thư mục mở hoặc chữ "Tải") để mở hộp thoại chọn tệp. Chọn một tệp `.json` chứa cấu hình bạn muốn tải.
*   **Lưu dạng...:** Nhấn nút này (biểu tượng lưu với dấu ba chấm hoặc chữ "Lưu dạng...") để lưu tất cả cài đặt hiện tại (bao gồm cả bản ghi) vào một tệp `.json` mới do bạn đặt tên và chọn vị trí.
*   **Lưu Hiện tại:** Nhấn nút này (biểu tượng lưu đơn giản hoặc chữ "Lưu") để lưu tất cả cài đặt hiện tại vào tệp `autokeyboard_config.json` mà ứng dụng đang sử dụng. Thao tác này sẽ ghi đè lên tệp đó.

## Cấu trúc thư mục dự án

```
autokeyboard/
├── assets/                 # Chứa các tài sản như icon ứng dụng
│   └── icon.ico
├── core/                   # Chứa logic cốt lõi của ứng dụng
│   ├── translations.py     # Quản lý đa ngôn ngữ
│   └── workers.py          # Các worker chạy ngầm cho auto-typing, hotkey, ghi/phát
├── gui/                    # Chứa mã nguồn giao diện người dùng (PySide6)
│   ├── autotyper_page.py   # Giao diện cho chế độ AutoTyper
│   ├── base_main_window.py # Cửa sổ chính cơ sở (khung, title bar, quản lý resize/drag)
│   ├── constants.py        # Các hằng số sử dụng trong GUI
│   ├── countdown_overlay.py# Lớp phủ đếm ngược khi ghi
│   ├── custom_title_bar.py # Thanh tiêu đề tùy chỉnh
│   ├── main_window.py      # Cửa sổ chính của ứng dụng, kế thừa từ BaseMainWindow
│   └── recorder_page.py    # Giao diện cho chế độ Ghi & Phát
├── linux-mac/              # Script chạy cho Linux và macOS
│   └── run.sh
├── venv/                   # (Thư mục môi trường ảo, được tạo tự động bởi script)
├── windows/                # Script chạy cho Windows
│   └── run.bat
├── .gitignore              # Các tệp và thư mục được Git bỏ qua
├── autokeyboard_config.json # Tệp cấu hình mặc định/được lưu của người dùng
├── main.py                 # Điểm vào chính của ứng dụng
└── requirements.txt        # Danh sách các thư viện Python cần thiết
```

## Công nghệ sử dụng

*   **Python:** Ngôn ngữ lập trình chính.
*   **PySide6:** Bộ thư viện Qt for Python, dùng để xây dựng giao diện người dùng đồ họa (GUI).
*   **pynput:** Thư viện để điều khiển và giám sát các thiết bị nhập liệu (bàn phím).

</details>

<!-- English -->
<details>
<summary>🇬🇧 English (Detailed)</summary>

## Overview

**AutoTyper Poetic** is a desktop application designed to automate keyboard input tasks. The application offers two main modes:
1.  **AutoTyper Mode:** Allows for repetitive typing of specific text or keys.
2.  **Recorder & Player Mode:** Enables recording complex sequences of keyboard actions and replaying them accurately.

Featuring a user-friendly interface built with Python and PySide6, along with the `pynput` library for handling keyboard interactions, AutoTyper Poetic provides a smooth and efficient experience.

## Important Notes

*   📜 **Configuration File:** All user settings (language, window size, hotkeys, recorded macros, etc.) are stored in the `autokeyboard_config.json` file in the application's root directory. This ensures your customizations are preserved across sessions.
*   🚀 **Automated Setup:** `run.bat` (for Windows) and `run.sh` (for Linux/macOS) scripts are provided to automate virtual environment creation (if not present) and dependency installation, helping you launch the application quickly.

## Key Features

*   **Flexible Dual-Mode Operation:**
    *   **AutoTyper Mode (Basic):**
        *   Automated typing of user-defined text or special keys (e.g., `<enter>`, `<f1>`, `<space>`).
        *   Adjustable typing interval (in milliseconds).
        *   Configurable repetition count (enter `0` for infinite).
        *   Dedicated hotkey (default **F9**, changeable) to start/stop auto-typing.
    *   **Recorder & Player Mode (Advanced):**
        *   Record sequences of keyboard actions (key presses, releases) with precise delays between them.
        *   Visual 3-second countdown overlay before recording starts, allowing you to prepare.
        *   Dedicated hotkeys (default **F10** for Record/Stop Record, **F11** for Play/Stop Play, changeable).
        *   Recorded actions are clearly displayed in a table (Key, Action, Delay).
        *   Playback of recorded sequences with adjustable repetition count (enter `0` for infinite).
        *   Option to **Clear Recording** to remove saved actions.
*   **Intuitive & User-Friendly Interface:**
    *   Modern, easy-to-use design built with PySide6.
    *   Custom title bar with standard window controls (minimize, maximize, close) and a customized look.
    *   Flexible window dragging and resizing support.
    *   Smooth animations for window open/close and mode transitions.
*   **Multilingual Support:**
    *   Interface available in English, Vietnamese (Tiếng Việt), and Japanese (日本語).
    *   Easy language switching via a dropdown menu in the title bar.
*   **Advanced Configuration Management:**
    *   All settings are persistently stored in `autokeyboard_config.json`.
    *   Stores language preference, window size/position, active mode (AutoTyper/Advanced), all hotkeys, AutoTyper settings, and recorded macros.
    *   Convenient functions: **Load Config** (from any `.json` file), **Save As...** (save current config to a new `.json` file), and **Save Current** (save to the currently used configuration file).
*   **Intelligent Hotkey Management:**
    *   Easy-to-use interface for changing hotkeys for AutoTyper, Record Start/Stop, and Playback Start/Stop.
    *   Automatic hotkey conflict detection to prevent assigning the same key to multiple actions, ensuring stable operation.
*   **Cross-Platform Compatibility:**
    *   Includes `run.bat` for Windows and `run.sh` for Linux/macOS to simplify setup and execution.
    *   These scripts automatically handle virtual environment creation and dependency installation.
*   **Clear Status Feedback:**
    *   Real-time status updates directly on the application interface.
    *   Visual countdown overlay when preparing to record.
    *   Detailed error and confirmation dialog boxes, making it easy for users to track and handle operations.

## Prerequisites (To run from source)

1.  **Python:** Python 3.x is recommended. The `run.bat`/`run.sh` scripts will attempt to use `python` (Windows) or `python3`/`python` (Linux/macOS) available in the system PATH.
2.  **Pip:** Python package installer (usually comes with Python).

## Installation & Running (From source)

The easiest and recommended way to run the application is by using the provided automation scripts:

### Using Scripts (Recommended)

1.  **Download Source Code:**
    *   Clone this repository or download it as a ZIP file and extract it.

2.  **Run the setup and launch script:**
    *   **On Windows:**
        1.  Navigate to the `windows` directory within the project's root folder.
        2.  Double-click to run the `run.bat` file.
    *   **On Linux/macOS:**
        1.  Open a Terminal.
        2.  Navigate to the `linux-mac` directory within the project's root folder.
        3.  Make the script executable: `chmod +x run.sh`
        4.  Run the script: `./run.sh`

    These scripts will automatically perform the following steps:
    *   Check for and create a Python virtual environment named `venv` in the project root (if it doesn't already exist).
    *   Activate the virtual environment.
    *   Install all necessary dependencies from the `requirements.txt` file.
    *   Launch the AutoTyper Poetic application.

### Manual Setup (Advanced Option)

If you prefer more granular control over the installation process:

1.  **Download Source Code** (as above).
2.  Open a Terminal or Command Prompt and navigate to the project's root directory.
3.  **(Recommended)** Create and activate a Python virtual environment:
    ```bash
    python -m venv venv
    ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the application:
    ```bash
    python main.py
    ```

## User Guide

Once the application is running:

### General Settings

*   **Switching Modes:** Use the **"Advanced"** / **"AutoTyper"** button on the title bar to toggle between the basic AutoTyper mode and the advanced Recorder & Player mode.
*   **Language Selection:** Use the language dropdown menu (e.g., "English", "Tiếng Việt", "日本語") on the title bar.

### AutoTyper Mode

1.  **Text/Key Input:** Enter the text you want to auto-type. For special keys, use the `<key_name>` format (e.g., `<enter>`, `<f12>`, `<space>`, `<ctrl>`, `<alt>`, `<shift>`).
2.  **Interval:** Set the time (in milliseconds) between each typed character or key press.
3.  **Repetitions:** Set the number of times to repeat the action (enter `0` for infinite repetitions).
4.  **AutoTyper Hotkey:**
    *   Defaults to **F9**.
    *   Click the **"Change Hotkey"** button to set a new hotkey. A prompt will ask you to press the desired key.
    *   Press this hotkey to **Start** or **Stop** the auto-typing process.
5.  **Start/Stop Buttons:**
    *   Click the **"Start (Hotkey_Name)"** button to begin.
    *   While running, this button will change to **"..."** (loading), and the **"Stop"** button will become active for you to halt the process.

### Recorder & Player Mode (Advanced)

1.  **Hotkey Configuration:**
    *   **Record/Stop Hotkey:** Defaults to **F10**. Used to start (after a 3-second countdown) and stop the recording process. Changeable via the **"Change Rec. Hotkey"** button.
    *   **Play/Stop Hotkey:** Defaults to **F11**. Used to start and stop playback of recorded actions. Changeable via the **"Change Play Hotkey"** button.
2.  **Repetitions (Playback):** Set the number of times you want the recorded action sequence to be played (enter `0` for infinite).
3.  **Recording Process:**
    *   Click the **"Start Recording (Record_Hotkey_Name)"** button or press the record hotkey.
    *   A countdown overlay will appear. After the countdown, all your key presses and releases will be recorded.
    *   Click the **"Stop Recording (Record_Hotkey_Name)"** button or press the record hotkey again to finish.
4.  **Playback Process:**
    *   Once a recording exists, click the **"Play Recording (Play_Hotkey_Name)"** button or press the play hotkey.
    *   To stop, click the **"Stop Playing (Play_Hotkey_Name)"** button or press the play hotkey again.
5.  **Clear Recording:** Click the **"Clear Recording"** button to delete all actions currently listed in the table. A confirmation dialog will appear.
6.  **Events Table:** Displays details of recorded keys, actions (Press/Release), and the delay (ms) between actions.

### Configuration Management

Configuration management buttons are located on the title bar:

*   **Load Config:** Click this button (folder open icon or "Load" text) to open a file dialog. Select a `.json` file containing the configuration you wish to load.
*   **Save As...:** Click this button (save icon with ellipsis or "Save As..." text) to save all current settings (including recordings) to a new `.json` file, for which you can specify the name and location.
*   **Save Current:** Click this button (simple save icon or "Save" text) to save all current settings to the `autokeyboard_config.json` file that the application is currently using. This will overwrite the file.

## Project Structure

```
autokeyboard/
├── assets/                 # Contains assets like the application icon
│   └── icon.ico
├── core/                   # Contains the core logic of the application
│   ├── translations.py     # Manages multilingual support
│   └── workers.py          # Background workers for auto-typing, hotkeys, recording/playback
├── gui/                    # Contains the user interface source code (PySide6)
│   ├── autotyper_page.py   # UI for AutoTyper mode
│   ├── base_main_window.py # Base main window (frame, title bar, resize/drag management)
│   ├── constants.py        # Constants used in the GUI
│   ├── countdown_overlay.py# Countdown overlay for recording
│   ├── custom_title_bar.py # Custom title bar
│   ├── main_window.py      # Main application window, inherits from BaseMainWindow
│   └── recorder_page.py    # UI for Recorder & Player mode
├── linux-mac/              # Run script for Linux and macOS
│   └── run.sh
├── venv/                   # (Virtual environment directory, auto-created by script)
├── windows/                # Run script for Windows
│   └── run.bat
├── .gitignore              # Files and directories ignored by Git
├── autokeyboard_config.json # Default/user-saved configuration file
├── main.py                 # Main entry point of the application
└── requirements.txt        # List of required Python libraries
```

## Technologies Used

*   **Python:** The primary programming language.
*   **PySide6:** Qt for Python bindings, used for building the graphical user interface (GUI).
*   **pynput:** A library for controlling and monitoring input devices (keyboard).

</details>

<!-- Japanese -->
<details>
<summary>🇯🇵 日本語 (詳細)</summary>

## 概要

**AutoTyper Poetic**は、キーボード入力タスクを自動化するために設計されたデスクトップアプリケーションです。このアプリケーションは、主に2つのモードを提供します:
1.  **オートタイパーモード:** 特定のテキストやキーを繰り返し入力できます。
2.  **レコーダー＆プレーヤーモード:** 複雑なキーボードアクションのシーケンスを記録し、正確に再生できます。

PythonとPySide6で構築されたユーザーフレンドリーなインターフェース、およびキーボードインタラクションを処理するための`pynput`ライブラリにより、AutoTyper Poeticはスムーズで効率的な体験を提供します。

## 重要な注意点

*   📜 **設定ファイル:** すべてのユーザー設定（言語、ウィンドウサイズ、ホットキー、記録されたマクロなど）は、アプリケーションのルートディレクトリにある`autokeyboard_config.json`ファイルに保存されます。これにより、カスタマイズ内容はセッション間で保持されます。
*   🚀 **自動セットアップ:** `run.bat`（Windows用）および`run.sh`（Linux/macOS用）スクリプトが提供されており、仮想環境の作成（存在しない場合）と依存関係のインストールを自動化し、アプリケーションを迅速に起動できます。

## 主な機能

*   **柔軟なデュアルモード操作:**
    *   **オートタイパーモード (基本):**
        *   ユーザー定義のテキストまたは特殊キー（例: `<enter>`, `<f1>`, `<space>`）の自動入力。
        *   調整可能な入力間隔（ミリ秒単位）。
        *   設定可能な繰り返し回数（無限の場合は`0`を入力）。
        *   自動入力を開始/停止するための専用ホットキー（デフォルト**F9**、変更可能）。
    *   **レコーダー＆プレーヤーモード (高度な設定):**
        *   キーボードアクションのシーケンス（キー押下、解放）とそれらの間の正確な遅延を記録。
        *   記録開始前に視覚的な3秒カウントダウンオーバーレイが表示され、準備が可能。
        *   専用ホットキー（記録/記録停止はデフォルト**F10**、再生/再生停止はデフォルト**F11**、変更可能）。
        *   記録されたアクションはテーブルに明確に表示（キー、アクション、遅延）。
        *   調整可能な繰り返し回数（無限の場合は`0`を入力）で記録されたシーケンスを再生。
        *   保存されたアクションを削除するための**「録画を消去」**オプション。
*   **直感的でユーザーフレンドリーなインターフェース:**
    *   PySide6で構築されたモダンで使いやすいデザイン。
    *   標準のウィンドウコントロール（最小化、最大化、閉じる）とカスタマイズされた外観を備えたカスタムタイトルバー。
    *   柔軟なウィンドウのドラッグとサイズ変更のサポート。
    *   ウィンドウの開閉およびモード移行時のスムーズなアニメーション。
*   **多言語サポート:**
    *   インターフェースは英語、ベトナム語（Tiếng Việt）、日本語（日本語）で利用可能。
    *   タイトルバーのドロップダウンメニューによる簡単な言語切り替え。
*   **高度な設定管理:**
    *   すべての設定は`autokeyboard_config.json`に永続的に保存されます。
    *   言語設定、ウィンドウのサイズ/位置、アクティブモード（オートタイパー/高度な設定）、すべてのホットキー、オートタイパー設定、記録されたマクロを保存。
    *   便利な機能: **「設定読込」**（任意の`.json`ファイルから）、**「名前を付けて保存...」**（現在の設定を新しい`.json`ファイルに保存）、**「現設定保存」**（現在使用中の設定ファイルに保存）。
*   **インテリジェントなホットキー管理:**
    *   オートタイパー、記録開始/停止、再生開始/停止のホットキーを変更するための使いやすいインターフェース。
    *   複数のアクションに同じキーが割り当てられるのを防ぐための自動ホットキー競合検出により、安定した操作を保証。
*   **クロスプラットフォーム互換性:**
    *   セットアップと実行を簡素化するためのWindows用`run.bat`とLinux/macOS用`run.sh`が付属。
    *   これらのスクリプトは、仮想環境の作成と依存関係のインストールを自動的に処理します。
*   **明確なステータスフィードバック:**
    *   アプリケーションインターフェース上でのリアルタイムのステータス更新。
    *   記録準備時の視覚的なカウントダウンオーバーレイ。
    *   詳細なエラーおよび確認ダイアログボックスにより、ユーザーは操作を簡単に追跡および処理できます。

## 前提条件（ソースから実行する場合）

1.  **Python:** Python 3.xを推奨します。`run.bat`/`run.sh`スクリプトは、システムのPATHで利用可能な`python`（Windows）または`python3`/`python`（Linux/macOS）を使用しようとします。
2.  **Pip:** Pythonパッケージインストーラー（通常Pythonに付属）。

## インストールと実行（ソースから）

アプリケーションを実行する最も簡単で推奨される方法は、提供されている自動化スクリプトを使用することです。

### スクリプトの使用 (推奨)

1.  **ソースコードのダウンロード:**
    *   このリポジトリをクローンするか、ZIPファイルとしてダウンロードして展開します。

2.  **セットアップおよび起動スクリプトの実行:**
    *   **Windowsの場合:**
        1.  プロジェクトのルートフォルダ内の`windows`ディレクトリに移動します。
        2.  `run.bat`ファイルをダブルクリックして実行します。
    *   **Linux/macOSの場合:**
        1.  ターミナルを開きます。
        2.  プロジェクトのルートフォルダ内の`linux-mac`ディレクトリに移動します。
        3.  スクリプトに実行権限を付与します: `chmod +x run.sh`
        4.  スクリプトを実行します: `./run.sh`

    これらのスクリプトは、次の手順を自動的に実行します:
    *   プロジェクトルートに`venv`という名前のPython仮想環境を確認し、存在しない場合は作成します。
    *   仮想環境をアクティブ化します。
    *   `requirements.txt`ファイルから必要なすべての依存関係をインストールします。
    *   AutoTyper Poeticアプリケーションを起動します。

### 手動セットアップ (高度なオプション)

インストールプロセスをより詳細に制御したい場合:

1.  **ソースコードをダウンロードします** (上記参照)。
2.  ターミナルまたはコマンドプロンプトを開き、プロジェクトのルートディレクトリに移動します。
3.  **(推奨)** Python仮想環境を作成してアクティブ化します:
    ```bash
    python -m venv venv
    ```
    *   Windowsの場合:
        ```bash
        venv\Scripts\activate
        ```
    *   Linux/macOSの場合:
        ```bash
        source venv/bin/activate
        ```
4.  必要な依存関係をインストールします:
    ```bash
    pip install -r requirements.txt
    ```
5.  アプリケーションを実行します:
    ```bash
    python main.py
    ```

## ユーザーガイド

アプリケーションの起動後:

### 一般設定

*   **モードの切り替え:** タイトルバーの**「高度な設定」** / **「オートタイパー」**ボタンを使用して、基本的なオートタイパーモードと高度なレコーダー＆プレーヤーモードを切り替えます。
*   **言語選択:** タイトルバーの言語ドロップダウンメニュー（例: 「日本語」、「English」、「Tiếng Việt」）を使用します。

### オートタイパーモード

1.  **テキスト/キー入力:** 自動入力したいテキストを入力します。特殊キーの場合は、`<key_name>`形式を使用します（例: `<enter>`、`<f12>`、`<space>`、`<ctrl>`、`<alt>`、`<shift>`）。
2.  **間隔:** 各文字入力またはキー押下の間の時間（ミリ秒）を設定します。
3.  **繰り返し回数:** アクションを繰り返す回数を設定します（無限に繰り返す場合は`0`を入力）。
4.  **オートタイパーホットキー:**
    *   デフォルトは**F9**です。
    *   **「ホットキー変更」**ボタンをクリックして新しいホットキーを設定します。目的のキーを押すようプロンプトが表示されます。
    *   このホットキーを押して、自動入力プロセスを**開始**または**停止**します。
5.  **開始/停止ボタン:**
    *   **「開始 (ホットキー名)」**ボタンをクリックして開始します。
    *   実行中は、このボタンは**「...」**（読み込み中）に変わり、**「停止」**ボタンがアクティブになり、プロセスを停止できます。

### レコーダー＆プレーヤーモード (高度な設定)

1.  **ホットキー設定:**
    *   **録画/停止ホットキー:** デフォルトは**F10**です。記録プロセスを開始（3秒のカウントダウン後）および停止するために使用します。**「録画ホットキー変更」**ボタンで変更可能です。
    *   **再生/停止ホットキー:** デフォルトは**F11**です。記録されたアクションの再生を開始および停止するために使用します。**「再生ホットキー変更」**ボタンで変更可能です。
2.  **繰り返し回数 (再生):** 記録されたアクションシーケンスを再生する回数を設定します（無限の場合は`0`を入力）。
3.  **記録プロセス:**
    *   **「録画開始 (録画ホットキー名)」**ボタンをクリックするか、録画ホットキーを押します。
    *   カウントダウンオーバーレイが表示されます。カウントダウン後、すべてのキー押下と解放が記録されます。
    *   **「録画停止 (録画ホットキー名)」**ボタンをクリックするか、再度録画ホットキーを押して終了します。
4.  **再生プロセス:**
    *   記録が存在する場合、**「再生 (再生ホットキー名)」**ボタンをクリックするか、再生ホットキーを押します。
    *   停止するには、**「再生停止 (再生ホットキー名)」**ボタンをクリックするか、再度再生ホットキーを押します。
5.  **録画を消去:** **「録画を消去」**ボタンをクリックすると、現在テーブルにリストされているすべてのアクションが削除されます。確認ダイアログが表示されます。
6.  **イベントテーブル:** 記録されたキー、アクション（押す/離す）、およびアクション間の遅延（ミリ秒）の詳細を表示します。

### 設定管理

設定管理ボタンはタイトルバーにあります:

*   **設定読込:** このボタン（フォルダを開くアイコンまたは「読込」テキスト）をクリックしてファイルダイアログを開きます。読み込みたい設定が含まれる`.json`ファイルを選択します。
*   **名前を付けて保存...:** このボタン（省略記号付きの保存アイコンまたは「名前を付けて保存...」テキスト）をクリックして、現在のすべての設定（記録を含む）を、名前と場所を指定できる新しい`.json`ファイルに保存します。
*   **現設定保存:** このボタン（シンプルな保存アイコンまたは「保存」テキスト）をクリックして、現在のすべての設定を、アプリケーションが現在使用している`autokeyboard_config.json`ファイルに保存します。これによりファイルが上書きされます。

## プロジェクト構成

```
autokeyboard/
├── assets/                 # アプリケーションアイコンなどのアセットを格納
│   └── icon.ico
├── core/                   # アプリケーションのコアロジックを格納
│   ├── translations.py     # 多言語サポートを管理
│   └── workers.py          # 自動入力、ホットキー、記録/再生のためのバックグラウンドワーカー
├── gui/                    # ユーザーインターフェースのソースコード (PySide6) を格納
│   ├── autotyper_page.py   # オートタイパーモードのUI
│   ├── base_main_window.py # 基本メインウィンドウ (フレーム、タイトルバー、リサイズ/ドラッグ管理)
│   ├── constants.py        # GUIで使用される定数
│   ├── countdown_overlay.py# 記録時のカウントダウンオーバーレイ
│   ├── custom_title_bar.py # カスタムタイトルバー
│   ├── main_window.py      # メインアプリケーションウィンドウ、BaseMainWindowを継承
│   └── recorder_page.py    # レコーダー＆プレーヤーモードのUI
├── linux-mac/              # LinuxおよびmacOS用実行スクリプト
│   └── run.sh
├── venv/                   # (仮想環境ディレクトリ、スクリプトによって自動作成)
├── windows/                # Windows用実行スクリプト
│   └── run.bat
├── .gitignore              # Gitによって無視されるファイルとディレクトリ
├── autokeyboard_config.json # デフォルト/ユーザー保存の設定ファイル
├── main.py                 # アプリケーションのメインエントリポイント
└── requirements.txt        # 必要なPythonライブラリのリスト
```

## 使用技術

*   **Python:** 主要なプログラミング言語。
*   **PySide6:** グラフィカルユーザーインターフェース（GUI）を構築するために使用されるPython用Qtバインディング。
*   **pynput:** 入力デバイス（キーボード）を制御および監視するためのライブラリ。

</details>

---
