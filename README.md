# <a href="with-grit.net" target="_blank">with GRIT</a>

<img width="200" alt="with-grit-logo" src="https://github.com/Ryo-Sasaki-xxx/front-with-grit/assets/118416144/6da83c51-be49-4c56-ab75-5c0544442322">

## with GRITとは
習慣化をカンタンにするをテーマに掲げ、目標設定、タスク設定、if-thenスケジュール設定をwebで可能にするサービスです！
「やり抜く人の九つの習慣」という書籍から影響をうけ、よりカンタンに実践できるように開発しました。
email: with-grit-test@test.com / pass: with-grit-testでテストアカウントとしてログインできます！一度<a href="with-grit.net" target="_blank">訪れて</a>みてください！

## こだわった点
- デザイン部分から力をいれて実装していきました。具体的にはfigmaを用いてモックから作成しデザイナーの友人から意見を貰いながら作成しました。
- 習慣化がしやすくなるように、将来的にはネイティブアプリとしても使っていただきたいので　SPAとapiでの実装としました。
- より多くの人に使ってほしいと思い、ホームページ等にも力を入れました。
- スマホ、タブレット等からも使えるようレスポンシブ対応をしました。

## 使用技術
- React(js)
   - styled-components
   - react-router-dom
   - axios
   - react-hook-form
   - etc.
- Django
  - DRF
- mysql 
- Nginx
- gunicorn
- Docker(Docker compose)
- gcp
- linux
- figma

## 機能
- ユーザー作成
- ゴールのcrud
- タスクのcrud
- if-thenの作成、更新
- ユーザー認証（jwt）
- ヘルプセンターでのお問い合わせ
- 管理者画面でのdb操作

## システム構成図
<img width="400" alt="with-grit-logo" src="https://github.com/Ryo-Sasaki-xxx/front-with-grit/assets/118416144/c464fe12-bb63-47f4-a748-172e93904907">
※gunicornは省略しています。
