#!/bin/bash
# Kiểm ngân sách dung lượng theo gói tài nguyên (chạy sau khi thêm map, quái, phái, thần tướng, ảnh mới).
cd "$(dirname "$0")/../.." || exit 1
export NODE_PATH=${NODE_PATH:-$(npm root -g)}
node cong_cu/claude/pack_dump.js /tmp/packs.json || exit 1
python3 cong_cu/claude/pack_budget.py /tmp/packs.json
