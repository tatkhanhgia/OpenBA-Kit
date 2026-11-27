# Chỉ mục đồ thị tri thức

Xuất nodes và edges vào `docs/knowledge-graph.json`. Thay các trường mẫu bằng ID và liên kết trích xuất từ hồ sơ dự án theo Rule 18.

```json
{
  "nodes": [{"id": "{source_id}", "type": "{source_type}"}, {"id": "{target_id}", "type": "{target_type}"}],
  "edges": [{"source": "{source_id}", "type": "depends_on", "target": "{target_id}"}]
}
```

Ghi loại cạnh theo trường nguồn (`depends_on` hoặc `related_diagrams`). Đánh dấu ID chưa tìm thấy trong bảng tra cứu.

| ID | Loại | Tài liệu nguồn | ID liên quan | Trạng thái liên kết |
|---|---|---|---|---|
| {id} | {type} | {path} | {target_id} | {status} |
