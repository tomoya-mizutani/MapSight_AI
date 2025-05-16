terminal :wsl  
python version is 3.12.3  
git version is 2.43.0.windows.1  

仮想環境: python3.12-venv  
起動コマンド: source ~/pubgmapenv/bin/activate   
終了コマンド:deactivate  


## 動画URLからフレーム抽出  
MapSight_AI/data　でコマンド実行．  
コマンド:  
YOUTUBE="https://www.youtube.com/watch?v=tkbV9EJPak4"     
ffmpeg -i "$(yt-dlp -f best -g "$YOUTUBE")" \
       -vf "fps=2,scale=1920:-2" -q:v 2 frames/frame_%05d.jpg  

・fps=2 → 0.5 s ごとに 1 枚（後で変更可能）  
・生成先 frames/ は後段スクリプトが再帰検索します。  
・画質を保ちたい場合は -q:v 2（2-31、数字が小さいほど高画質）。  

