# ibus-icon-customize
Script thay đổi icon cho ibus, dùng để thay đổi icon cho bamboo và tiếng anh mặc định. Dùng cho các distro có DE là KDE.
## Hướng dẫn:
Cách dùng:  `make [OPTIONS] [c=[0x000000-0xffffff]]`

|  Options:          | Mô tả: |
|:-------------------|:-------------|
| install            | Cài đặt thư mục hiện tại làm thư mục chứa icon chỉ cần chạy 1 lần|
| default            | Thay đổi icon thành mặc định (icon này mình tự vẽ)|
| flag               | Thay đổi icon thành lá cờ |
| flag-circle        | Thay đổi icon thành lá cờ bo tròn |
| color c=[0x000000-0xffffff]    | Thay đổi icon thành icon mặc định với màu được chỉ định |
| text c=[0x000000-0xffffff]     | Thay đổi icon thành chữ với màu được chỉ định |
| help               | Hiện ra hộp thoại này |

_Nếu không đưa ra option nào thì hộp thoại này sẽ hiện ra_

__MẸO: KDE có widget là color picker(chạy nó tron krunner) dùng để xác định màu của bất cứ thứ gì trên màn hình, bạn hãy lấy giá trị HEX của màu theme của bạn và pass nó vào c=0x...__
