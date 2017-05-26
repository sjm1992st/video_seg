#!/usr/bin/python
#coding:utf-8


import os
import xml.dom.minidom
import xml.sax
import cv2
import time
import ctypes
import re
dll = ctypes.cdll.LoadLibrary( 'opencv_ffmpeg2410_64.dll' )

def write_xml(vname,mpath,kk,k,mdata):
    #在内存中创建一个空的文档
    doc = xml.dom.minidom.Document()
    #创建一个根节点Managers对象
    root = doc.createElement('VClip')
    #设置根节点的属性
    ##root.setAttribute('name', vname)
    #将根节点添加到文档对象中
    mlabel=mdata[k]['label']
    mroi=mdata[k]['roi']

    doc.appendChild(root)
    nodeName0 = doc.createElement('name')
    nodeName0.appendChild(doc.createTextNode(str((vname).decode('gbk').encode("utf-8"))))
    nodeDomain=doc.createElement('domain')
    nodeDomain.appendChild(doc.createTextNode('football'))
    nodeLabel = doc.createElement("name")
    nodeLabel.appendChild(doc.createTextNode(str((mlabel).encode("utf-8"))))
    root.appendChild(nodeName0)
    root.appendChild(nodeDomain)
    nodeManager0=doc.createElement("sublabel")
    nodeLabel_=doc.createElement("label")
    nodeLabel_.appendChild(nodeLabel)
    if kk==-1:
        mstart0=int(mdata[k]['start'])
        mend0=int(mdata[k]['end'])
        msublabe0=mdata[k]['sublabel']
        SubName0 = doc.createElement('name')
        SubName0.appendChild(doc.createTextNode(str((msublabe0).encode("utf-8"))))
        nodeStart0 = doc.createElement('start')
        #给叶子节点name设置一个文本节点，用于显示文本内容
        nodeStart0.appendChild(doc.createTextNode(str(mstart0)))
        nodeEnd0 = doc.createElement("end")
        nodeEnd0.appendChild(doc.createTextNode(str(mend0)))
        #将各叶子节点添加到父节点Manager中，
        #最后将Manager添加到根节点Managers中
        nodeManager0.appendChild(SubName0)
        nodeManager0.appendChild(nodeStart0)
        nodeManager0.appendChild(nodeEnd0)
        nodeLabel_.appendChild(nodeManager0)
    else:
        mstart0=int(mdata[k]['start'])
        mend0=int(mdata[k]['end'])
        msublabe0=mdata[k]['sublabel']
        SubName0 = doc.createElement('name')
        SubName0.appendChild(doc.createTextNode(str((msublabe0).encode("utf-8"))))
        nodeStart0 = doc.createElement('start')
        #给叶子节点name设置一个文本节点，用于显示文本内容
        nodeStart0.appendChild(doc.createTextNode(str(mstart0)))
        nodeEnd0 = doc.createElement("end")
        nodeEnd0.appendChild(doc.createTextNode(str(mend0)))
        #将各叶子节点添加到父节点Manager中，
        #最后将Manager添加到根节点Managers中
        nodeManager0.appendChild(SubName0)
        nodeManager0.appendChild(nodeStart0)
        nodeManager0.appendChild(nodeEnd0)
        nodeLabel_.appendChild(nodeManager0)
        nodeManager1=doc.createElement("sublabel")
        mstart1=int(mdata[kk]['start'])
        mend1=int(mdata[kk]['end'])
        msublabe1=mdata[kk]['sublabel']
        SubName1 = doc.createElement('name')
        SubName1.appendChild(doc.createTextNode(str((msublabe1).encode("utf-8"))))
        nodeStart1 = doc.createElement('start')
        #给叶子节点name设置一个文本节点，用于显示文本内容
        nodeStart1.appendChild(doc.createTextNode(str(mstart1)))
        nodeEnd1 = doc.createElement("end")
        nodeEnd1.appendChild(doc.createTextNode(str(mend1)))
        #将各叶子节点添加到父节点Manager中，
        #最后将Manager添加到根节点Managers中
        nodeManager1.appendChild(SubName1)
        nodeManager1.appendChild(nodeStart1)
        nodeManager1.appendChild(nodeEnd1)
        nodeLabel_.appendChild(nodeManager1)


    nodeRoi = doc.createElement("roi")
    nodeRoi.appendChild(doc.createTextNode(str(mroi)))
    nodeLabel_.appendChild(nodeRoi)


    root.appendChild(nodeLabel_)
    #开始写xml文档
    ##print chardet.detect(mpath)
    fp = open(mpath,'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.name = ""
      self.mdata=[]


   # 元素开始事件处理
   def startElement(self, tag, attributes):
      self.CurrentData = tag

      if tag == "VClip":
         self.mdata.append(attributes)

   # 元素结束事件处理
   def endElement(self, tag):
        pass


   # 内容事件处理
   def characters(self, content):
        pass

def scan_files(directory,prefix=None,postfix=None):
  files_list=[]

  ##Ndata = pd.read_table(frame_path,header=None,delim_whitespace=True,index_col=False)
  for root, sub_dirs, files in os.walk(directory):
    for special_file in files:
      if postfix:
        if special_file.endswith(postfix):
          files_list.append(os.path.join(root,special_file))
      elif prefix:
        if special_file.startswith(prefix):
          files_list.append(os.path.join(root,special_file))
      else:
        files_list.append(os.path.join(root,special_file))

  return files_list

def rep(Mtxt_path,xx):
    if not os.path.exists(Mtxt_path):
        fpw = open(Mtxt_path,'w')
        fpw.close()
    fpw = open(Mtxt_path,'r')
    Nane_str=fpw.readlines()
    #print Nane_str[0]
    fpw.close()
    if (xx+'\n') in Nane_str:
        print 'yy'
        return False
    else:
        print 'nn'
        fpw = open(Mtxt_path,'a+')
        fpw.writelines(xx+'\n')
        fpw.close()
        return True

def generate_action_dataset(original_path,new_path):

    ##path_xml = sys.argv[2]

    # 第一个输入参数是包含视频片段的路径
    ##input_path = sys.argv[1]
    ##input_path="E:\\pythonworkspace\\video_seg\\mkv"
    ##print input_path,path_xml
    # 第二个输入参数是设定每隔多少帧截取一帧
    frame_interval = 0

    # 列出文件夹下所有的视频文件
    ##filenames = os.listdir(original_path)
    filenames=scan_files(original_path)
    # 获取文件夹名称
    video_prefix = original_path.split(os.sep)[-1]
    Mtxt_path=original_path+'\\'+'VideoName.txt'
    ##if not os.path.exists(frame_path):

    # 建立一个新的文件夹
    frame_path =new_path
    if not os.path.exists(frame_path):
        os.mkdir(frame_path)

    # 初始化一个VideoCapture对象
    cap = cv2.VideoCapture()
    # 遍历所有文件
    ki=0

    mcout_label={}
    for filename in filenames:
        (shotname,extension) = os.path.splitext(filename)
        if(extension=='.mkv'):
            ki=ki+1
            filepath = filename
            NewName=shotname.split(os.sep)[-1]
            print "==============================================="
            time.sleep(1)

            print 'NO.'+str(ki)+'--'+filepath.decode('gbk')
            time.sleep(1)

            path_xml=shotname+'.xml'

            if not os.path.isfile(path_xml):
                print "not xml"

                continue

            # 创建一个 XMLReader
            parser = xml.sax.make_parser()
            # turn off namepsaces
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)

            # 重写 ContextHandler
            Handler = MovieHandler()
            parser.setContentHandler( Handler )
            parser.parse(path_xml)
            ##print Handler.mdata["end"]
            # VideoCapture::open函数可以从文件获取视频
            Handler.mdata.sort(key=lambda k: (int(k.get('start')), int(k.get('end'))))
            cap.open(filepath)
            # 获取视频帧数CAP_PROP_FRAME_COUNT
            n_frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
            #获得码率及尺寸
            fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
            size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
                    int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

            #指定写视频的格式, I420-avi, MJPG-mp4
            """
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,19821)
            success1, frame1 = cap.read()
            ii=0
            videoWriter1 = cv2.VideoWriter('19821.mkv', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
            while(ii<61):
                videoWriter1.write(frame1) #写视频帧
                cv2.waitKey(100/int(fps)) #延迟
                ii=ii+1
                success1, frame1 = cap.read()
            """

            print n_frames
            time.sleep(1)
            #trigger.emit(str(n_frames))
            mlen=len(Handler.mdata)
            Rnum=range(mlen)
            while(len(Rnum)>0):
                k=Rnum[0]
                mstart=int(Handler.mdata[k]['start'])
                mend=int(Handler.mdata[k]['end'])
                mlabel=Handler.mdata[k]['label']
                msublabel=Handler.mdata[k]['sublabel']
                mroi=Handler.mdata[k]['roi']
                Rnum.remove(k)
                Flag_=0
                for kk in Rnum:
                    mstart2=int(Handler.mdata[kk]['start'])
                    mend2=int(Handler.mdata[kk]['end'])
                    mlabel2=Handler.mdata[kk]['label']
                    msublabel2=Handler.mdata[kk]['sublabel']
                    mroi2=Handler.mdata[kk]['roi']
                    if abs(mend-mstart2)<=3 and mlabel2==mlabel:
                        Rnum.remove(kk)
                        mend=mend2
                        Flag_=1
                        break
                if Flag_==0:
                    kk=-1
                    if re.search(u'准备', msublabel):
                        continue
                i=0
                pp=mend-mstart
                if pp<min_frame:
                    continue
                cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,mstart)
                Mflag=0
                while(i<mend-mstart+2):

                    success, frame = cap.read()
                    xx=NewName+'_'+(mlabel).encode('gbk')+'_'+str(mstart)+'_'+str(mend)
                    if i==0:
                        gbk_frame_path=frame_path+'\\'+(mlabel).encode('gbk')
                        if not os.path.exists(gbk_frame_path):
                            os.mkdir(gbk_frame_path)
                        mfileName=gbk_frame_path+'\\'+NewName+'_'+(mlabel).encode('gbk') +'_'+str(mstart)+'_'+str(mend)+'.mkv'
                        if (rep(Mtxt_path,xx)):
                            Mflag=1
                            ##print kc,len(Handler.mdata)
                            videoWriter = cv2.VideoWriter(mfileName, cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
                        else:
                            break
                        print ' ready---'+mfileName
                        print '1',mstart
                        temp2_str=' ready---'+mfileName
                        time.sleep(1)

                        ##print fps
                    if success and i>=0:
                        ##cv2.imshow("Oto Video", frame) #显示
                        if Mflag==1:
                            videoWriter.write(frame) #写视频帧
                            cv2.waitKey(100/int(fps)) #延迟
                        else:
                            break

                    i=i+1
                if Mflag==1:
                    x_name=gbk_frame_path+'\\'+NewName+'_'+(mlabel).encode('gbk')+'_'+str(mstart)+'_'+str(mend)
                    xml_name=gbk_frame_path+'\\'+NewName+'_'+(mlabel).encode('gbk')+'_'+str(mstart)+'_'+str(mend)+'.xml'
                    write_xml(x_name,xml_name,kk,k,Handler.mdata)





    cap.release()

###################################################
original_path='E:\\pythonworkspace\\video_seg\\ysv'
new_path='E:\\pythonworkspace\\video_seg\\ood'
min_frame=11
generate_action_dataset(original_path,new_path)