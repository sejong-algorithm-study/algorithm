# ๐ป Commit Message ๊ท์น
1. ์ปค๋ฐ ์ด์ ์ ๋จผ์  `upstream` repository ์ ๋๊ธฐํ๋ฅผ ์์ผ์ฃผ์ธ์.   
   

    $ git pull upstream main


2. ์ปค๋ฐ ๋ฉ์์ง๋ ```[๋ฌธ์  ์ถ์ฒ ์ฌ์ดํธ] ๋ฌธ์  ๋ฒํธ : ๋ฌธ์  ์ด๋ฆ ``` ๋ก ํด์ฃผ์ธ์.
   

      $ git commit -m [BOJ] 12345 : Moist (Small2)

# ๐ป Pull Request ๊ท์น
1. fork ํ ๊ฐ์ธ repository ์์ upstream repository์ `main` ๋ธ๋์น๋ก pull request ๋ฅผ ํด์ฃผ์ธ์.
   
    - `compare across forks` ๋ฅผ ๋๋ฆ๋๋ค.
    - ๋ณธ์ธ repo๊ฐ `compare`, upstream repo๊ฐ `base`๋ก ์์นํ๊ฒ ์ ํ
    - `create pull request` ๋ฅผ ๋๋ฌ์ฃผ์ธ์.
          ![img.png](img.png)
2. pull request ๋ฉ์์ง ์ ๋ชฉ์ `[YYYY.MM.DD] ๋ฌธ์  ์ถ์ฒ ์ฌ์ดํธ ๋ฌธ์  ๋ฒํธ <ํผ ์ธ์ด>` ๋ก ํต์ผํด์ฃผ์ธ์.
   

    [2021.01.01] PROGRAMMERS 12345 <python>
3. ๊ท์น์ด ๋ง๋ค๋ฉด ํ๋ฃจ ์ด๋ด์ pull request ๊ฐ ์๋ฝ๋ฉ๋๋ค. (๊ท์น๊ณผ ๋ง์ง ์์ผ๋ฉด ๋ฐ๋ ค๋  ์ ์์ต๋๋ค.)