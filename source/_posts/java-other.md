---
title: Java Other
tags: java
date: 2019-12-22
---

### Java PlaySound

播放 mp3 音乐, 需要添加 mp3plugin.jar

```java
package com.jbn.example.other;

import javax.sound.sampled.*;
import java.io.IOException;
import java.io.InputStream;

public class PlaySound {
     public static void main(String ... args){
         try {
             Clip clip = AudioSystem.getClip();
             // 资源的放置位置, 非 maven 项目直接放在 src 下, maven 项目放在与 src 同级的 resource 下
             InputStream inputStream = PlaySound.class.getClassLoader().getResourceAsStream("sound/snake.wav");
             // java.io.IOException: mark/reset not supported ???
             // InputStream inputStream = new FileInputStream("/Users/jbn/Desktop/study/java/basic/src/sound/snake.wav");
             AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(inputStream);
             clip.open(audioInputStream);
             clip.start();
             clip.loop(Clip.LOOP_CONTINUOUSLY);
             Thread.sleep(100000);
             clip.stop();
         } catch (LineUnavailableException | UnsupportedAudioFileException | IOException | InterruptedException e) {
             e.printStackTrace();
         }
     }
}
```