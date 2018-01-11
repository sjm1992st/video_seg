##本代码是实习时为视频动作识别项目写的制作训练数据集的代码，前期是人工标注，标注结果得到时标注信息xml文件，下面是根据标注文件xml对视频进行片段切分
### 视频片段提取代码
#### 输入视频文件.mkv和标注文件信息.xml，根据标注文件[xml](https://github.com/sjm1992st/video_seg/blob/master/picture/(0623_%E6%84%8F%E5%A4%A7%E5%88%A9_%E7%88%B1%E5%B0%94%E5%85%B0_1st_half).xml)中的帧位置信息提取相应片段，保存到输出路径下，示例如下：
主程序video_seg.py <br>
![Alt text](https://github.com/sjm1992st/video_seg/blob/master/picture/1.PNG) <br>
程序输出-- 程序自动根据xml中的标签自动为每个标签分别建立文件夹，如下 <br>
![Alt text](https://github.com/sjm1992st/video_seg/blob/master/picture/4.PNG) <br>
程序根据xml标注信息切分视频文件，将切分得到的动作片段自动存放到对应的标签文件夹下：[xml](https://github.com/sjm1992st/video_seg/blob/master/picture/(0623_%E6%84%8F%E5%A4%A7%E5%88%A9_%E7%88%B1%E5%B0%94%E5%85%B0_1st_half)_%E7%90%83%E9%97%A8%E7%90%83_29370_29454.xml)<br>
![Alt text](https://github.com/sjm1992st/video_seg/blob/master/picture/5.PNG)
