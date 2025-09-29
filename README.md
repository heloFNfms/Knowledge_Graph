> 主要针对两个或多个Java环境如何在一个计算机中不冲突，会发现我们配置环境变量只能识别一个Java环境

## 1 .编写`.bat`文件

  主要告诉要启动的程序，我接下来要使用计算机中的哪个`Java`环境。

  ### 下面以neo4j来举例子

  当我安装了`neo4j-community-5.24.1-windows`，但是我的计算机中的环境变量中配置的是`Java8`的，所以启动这个`neo4j`的时候会报错。要解决这个错误最原始的方式就是替换环境变量中的`Java`环境的位置。

  下面通过编写.bat文件来方便 `neo4j `知道使用哪个Java版本来启动。

  ```Python
@echo off
chcp 65001 >nul
echo ========================================
echo 正在为Neo4j设置Java 17环境...
echo ========================================

REM 设置Java 17路径
set JAVA_HOME=D:\java17 jdk
set PATH=%JAVA_HOME%\bin;%PATH%

echo 当前Java版本：
java -version
echo.
echo ========================================
echo 启动Neo4j...
echo ========================================

REM 进入Neo4j的bin目录
cd /d "%~dp0bin"
neo4j.bat console

echo.
echo Neo4j已停止运行
pause
```


  在这个neo4j的文件夹根目录下编写一个.bat文件，然后将上面的代码中的Java路径替换为自己的路径，点击运行就可以了。

## 2.通过 Docker 来实现

  这个相对方便，但前提你有 Docker，它充当一个容器，把服务封装好。下面还是以`neo4j`来作为例子

  ```Python
docker run -d   
  --name neo4j-container
  -p 7474:7474 -p 7687:7687   
   -e NEO4J_AUTH=neo4j/WZY216814wzy
   neo4j:5.24.1
```


  这相当于Docker已经帮你在容器中配置好了运行 neo4j 的运行环境，完全和你的计算机中的环境进行隔离。 
  
  <img width="1919" height="1078" alt="屏幕截图 2025-09-29 105903" src="https://github.com/user-attachments/assets/f6c80d95-065f-4e28-83e4-8dd311c77fbe" />


