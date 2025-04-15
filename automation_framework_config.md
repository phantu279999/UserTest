
# 📘 Automation Framework - Configuration Reference

## 🧩 `type_action`  
Danh sách các hành động có thể thực hiện trong test case:

- `get_domain`  
- `open_new_tab`  
- `click`  
- `input`  
- `input_enter`  
- `enter`  
- `switch_to_frame`  
- `switch_to_next_tab`  
- `switch_to_last_tab`  
- `switch_to_first_tab`  
- `move`  
- `move_click`  
- `drag_and_drop`  
- `clear`  
- `clear_and_input`

---

## 📌 `element_action`  
Thuộc tính hỗ trợ cho mỗi action:

- `name`: Tên step (tuỳ chọn)
- `type`: Loại action (`type_action`)
- `locator`: Selector để định vị element
- `locator_type`: Kiểu locator (mặc định là `xpath`)
- `value`: Giá trị nhập hoặc URL
- `sleep`: Delay sau mỗi action (ms hoặc giây)
- `result`: Điều kiện kiểm tra sau step
- `locator_2`: Dùng trong các thao tác kéo thả (drag & drop)
- `locator_type_2`: Kiểu locator thứ hai (mặc định `xpath`)

---

## 🧭 `type_locator`  
Các loại `locator_type` được hỗ trợ:

- `id`
- `xpath` *(default)*
- `link text`
- `partial link text`
- `name`
- `tag name`
- `class name`
- `css selector`

---

## ✅ `type_result`  
Các kiểu kiểm tra kết quả sau một bước:

### `title`
> Kiểm tra tiêu đề trang web

```json
{
  "type": "title",
  "value": "Hello World!"
}
```

---

### `xpath`
> Kiểm tra một element tồn tại trong DOM

```json
{
  "type": "xpath",
  "xpath": "//h1"
}
```

---

### `display`
> Kiểm tra một element có hiển thị hay không

```json
{
  "type": "display",
  "xpath": "//h1"
}
```

---

### `xpath_text`
> Kiểm tra nội dung text của một element

```json
{
  "type": "xpath_text",
  "xpath": "//h1",
  "value": "Hello Everybody"
}
```

---

### `url`
> Kiểm tra URL hiện tại

```json
{
  "type": "url",
  "value": "https://example.vn"
}
```

---

### `alert`
> Kiểm tra alert có xuất hiện hay không

```json
{
  "type": "alert",
  "status": true
}
```

---

### `status`
> Kiểm tra mã trạng thái HTTP (status code)

```json
{
  "type": "status",
  "value": 404
}
```
