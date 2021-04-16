# ibus-icon-customize-for-vietnamese
Script thay đổi icon cho ibus, dùng để thay đổi icon cho bamboo tiếng việt và tiếng anh mặc định. Dùng cho các distro có DE là KDE (GNOME không dùng được do nó mặc định xài icon là chữ theo panel).
## Hướng dẫn:
Cách dùng:  `make [OPTIONS] [c=[0x000000-0xffffff]]`

|  Options:          | Mô tả: |
|:-------------------|:-------------|
| install            | Cài đặt thư mục hiện tại làm thư mục chứa icon chỉ cần chạy 1 lần và phải tự restart ibus bằng `ibus restart`|
| default            | Thay đổi icon thành mặc định (icon này mình tự vẽ)|
| flag               | Thay đổi icon thành lá cờ |
| flag-circle        | Thay đổi icon thành lá cờ bo tròn |
| color c=[0x000000-0xffffff]    | Thay đổi icon thành icon mặc định với màudạng HEX được chỉ định |
| text c=[0x000000-0xffffff]     | Thay đổi icon thành chữ với màu dạng HEX được chỉ định |
| help               | Hiện ra hộp thoại này |

_Nếu không đưa ra option nào thì hộp thoại này sẽ hiện ra_

## Mẹo:
1. KDE có widget là color picker(chạy nó tron krunner) dùng để xác định màu của bất cứ thứ gì trên màn hình, bạn hãy lấy giá trị HEX của màu theme của bạn và pass nó vào c=0x...
2. Bạn có thể tự vẽ icon và thay thế 2 file vi.svg và us.svg (2 file này sinh ra sau khi cài đặt) sau đó restart ibus bằng `ibus restart` để thấy sự thay đổi.
