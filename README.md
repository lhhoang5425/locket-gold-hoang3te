<p align="center">
  <a href="https://lhhoang5425.github.io/nocket-gay-hoang3te/" target="_blank">
    <img src="https://i.pinimg.com/736x/d4/42/64/d4426485d809524bf737bab3964144ae.jpg" width="96" height="96" style="border-radius: 22px; object-fit: cover;" alt="Zekas VIP Hub Logo"/>
  </a>
</p>

# <p align="center">Zekas VIP Hub</p>

<p align="center">
  <em>Hệ thống cấu hình tối ưu Shadowrocket và mô-đun mở khóa tính năng cao cấp</em>
</p>

---

> [!WARNING]
> **Tuyên bố miễn trừ trách nhiệm (Disclaimer):**  
> Dự án được phát triển phục vụ mục đích nghiên cứu kỹ thuật, học tập cá nhân và phân tích luồng mạng (Network Traffic Analysis). Nghiêm cấm mọi hình thức khai thác thương mại hóa. Cre : Zekas Dev

## Cấu trúc

| Đường dẫn | Nội dung |
| --- | --- |
| `index.html` | Web Hub (GitHub Pages) |
| `Config/Locket_Zekas.conf` / `.sgmodule` | Cấu hình + mô-đun Locket Gold Zekas |
| `Locket/LocketGold.mobileconfig` | Hồ sơ DNS chống thu hồi |
| `js/Locket/` | Script RevenueCat + Remote Config |
| `version.json` | Phiên bản hub và thông tin IPA phát hành |

## Nguồn tải

Web Hub hỗ trợ 2 nguồn, chọn bằng nút **GitHub / jsDelivr**:

- GitHub: `https://raw.githubusercontent.com/lhhoang5425/nocket-gay-hoang3te/main`
- jsDelivr: `https://cdn.jsdelivr.net/gh/lhhoang5425/nocket-gay-hoang3te@main`

**jsDelivr** là CDN phản chiếu GitHub: giúp tải nhanh và ổn định hơn khi `raw.githubusercontent.com` bị chặn, nhưng có thể cache chậm tới ~12 giờ. Mặc định dùng GitHub để nhận cập nhật tức thì.

## Cập nhật & phát hành

1. Sửa nội dung → tăng `APP_VERSION` trong `index.html` và `version` trong `version.json`.
2. Push lên `main`: GitHub Pages (deploy từ branch) tự cập nhật, workflow `Validate` kiểm tra JS/JSON/plist và file được tham chiếu.
3. Khi có IPA: điền object `ipa` vào `version.json` (Card 5 sẽ tự hiện):

```json
{
  "ipa": {
    "version": "1.0.0",
    "url": "https://github.com/lhhoang5425/nocket-gay-hoang3te/releases/download/v1.0.0/Locket-Zekas.ipa",
    "size": "48 MB",
    "min_ios": "15.0",
    "sha256": "..."
  }
}
```
