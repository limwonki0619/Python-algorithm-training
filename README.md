# Algorithm-training
 - 기초적인 알고리즘을 학습합니다.
 - 알고리즘 예제 사이트는 다음과 같습니다. 
 > [1. 초코몽키](https://wayhome25.github.io/#python)님의 알고리즘 예제  
 > [2. 알고리즘 히어로즈](https://level.goorm.io/)의 알고리즘 예제  
 > [3. Baekjoon Online Judge](https://www.acmicpc.net/)의 알고리즘 예제  
 > [4. codility](https://app.codility.com/programmers/)의 알고리즘 예제  
 > [5. 파이썬 300제](https://wikidocs.net/7003)의 기초 단련 예제   
 > [6. 코딩도장](http://codingdojang.com/list/1?sort=level&sort_order=fw)의 알고리즘 예제  
 
# Jupyter-Notebook 
 - 파이썬 코드를 확인하고자 `Jupyter Notebook`을 사용합니다
 - `Jupyter Notebook`에 관한 기본 설정은 다음과 같습니다.
 
### Jupyter Notebook 디렉토리 변경방법 
 > 1. `cmd`를 실행합니다. 
 > 2. cmd창에 `jupyter notebook --generate-config`를 입력 한 후  `jupyter_notebook_config.py` 파일의 위치를 확인합니다. 
 > 3. 파일위치에서 `jupyter_notebook_config.py`파일을 엽니다. (VS CODE, 파이참 등등)
 > 4. Ctrl+F를 통해 `#c.NotebookApp.notebook_dir` 를 찾습니다. 
 > 5. `#c.NotebookApp.notebook_dir = ' '`에서 `' '` 사이에 원하는 절대 경로를 설정해줍니다. (단, 경로설정시 `\`를 `/`로 변경해야 합니다.) 
 > 6. 경로설정 후 앞에있는 주석(`#`)을 없애고 파일을 저장합니다.
 > 7. `Jupyter Notebook`을 재실행 한 후 기본 디렉토리를 확인합니다. 
 
### Jupyter Notebook 테마 적용 방법 
 > 1. `Anaconda`를 사용하는 환경에서는 `windows 시작버튼 -> Anaconda Prompt`를 실행합니다.  
 > 2. 프롬프트 창에 `pip install jupyterthemes`를 입력하고 테마를 다운로드 합니다.   
 > 3. 적용가능한 테마는 `jt -l(소문자 엘)`로 확인할 수 있습니다.  
 > 4. 참고로 적용가능한 옵션은 [여기](https://github.com/dunovank/jupyter-themes/blob/master/README.md)에서 확인할 수 있습니다.
 > 5. 많은 옵션 가운데 `jt -t monokai -f hack -fs 12 -T -N`이 정도만 입력해도 충분합니다.
 > + *옵션설명 : 테마(t)는 monokai, 폰트(f)는 hack, 폰트사이즈(fs)는 8, 툴바보이기(T), 이름&로고보이기(N) 옵션 적용* 
 > 6. 옵션적용을 마치면 `Anaconda Navigator`를 통해 `Jupyter notebook`을 실행 합니다.
 > 7. 만약 초기화를 원한다면 `Anaconda prompt`창에 `jt -r`를 입력하면 됩니다.  
 > ~~만약 새로운 테마를 적용하거나 기존 테마로 되돌리고자 한다면 기존 `~/.jupyter`위치의`custom`파일을 삭제 한 후 다시 적용하면 됩니다.~~
 > + 다만, 파이플롯으로 그래프를 그리면 바탕이 어두워 축의 숫자가 잘 안보일 수 있는데, 이럴 경우 <bR>
 > `fig = plt.figure()`와 `fig.patch.set_facecolor('xkcd:white')`를 입력해주면 흰색배경의 그림을 그릴 수 있습니다. 
 > + 출처는 [여기](https://woongheelee.com/entry/주피터-노트북-Jupyter-Notebook-테마-바꾸기-어둡게)입니다. 

