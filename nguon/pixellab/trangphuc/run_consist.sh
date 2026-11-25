#!/bin/sh
# 7 nhóm 3 khung còn lại của hàng y=256 (ô 0-7, 11-23), cùng seed 5; chạy tối đa 3 nhóm song song
cd /home/user/HoaThan/nguon/pixellab
printf '%s\n' \
 "0,256 160,256 320,256" "480,256 640,256 800,256" "960,256 1120,256 1760,256" \
 "1920,256 2080,256 2240,256" "2400,256 2560,256 2720,256" "2880,256 3040,256 3200,256" "3360,256 3520,256 3680,256" \
| xargs -P3 -I{} sh -c 'python3 trangphuc/gen_consist.py nam c1 5 $(echo {} | sed "s/ / /g") 2>&1 | tail -2'
echo ALLDONE
