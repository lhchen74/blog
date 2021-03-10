---
title: java robot
tags: java
date: 2020-07-09
---

可以使用 java 的 robot 操纵鼠标，键盘做一些重复机械的工作

```java
package com.jbn.learn;

import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;

public class RobotTest
{
    
    public static void sendKeys(Robot robot, String keys) throws InterruptedException {
        for (char c : keys.toCharArray()) {
            int keyCode = KeyEvent.getExtendedKeyCodeForChar(c);
            if (KeyEvent.CHAR_UNDEFINED == keyCode) {
                throw new RuntimeException(
                        "Key code not found for character '" + c + "'");
            }
            robot.keyPress(keyCode);
            robot.keyRelease(keyCode);
			robot.delay(100);
        }
    }
    
    public static void sendKeysByClipBoard(Robot robot, String text) {
        StringSelection stringSelection = new StringSelection(text);
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        clipboard.setContents(stringSelection, stringSelection);
        robot.keyPress(KeyEvent.VK_CONTROL);
        robot.keyPress(KeyEvent.VK_V);
        robot.keyRelease(KeyEvent.VK_V);
        robot.keyRelease(KeyEvent.VK_CONTROL);
        robot.delay(100);
    }


    public static void main(String[] args) throws IOException,
            AWTException, InterruptedException
    {
        int shortDelayTime  = 100;
        int middleDelayTime = 5000;
        int normalDelayTime = 10000;
        int largeDelayTime = 15000;

        // Launch IE
        String command = "C:\\Program Files\\Internet Explorer\\iexplore.exe";
        Runtime run = Runtime.getRuntime();
        run.exec(command);
        Thread.sleep(normalDelayTime);

        // Create an instance of Robot class
        Robot robot = new Robot();

        // Locate input box and delete input text
        robot.mouseMove(100, 40);
        robot.delay(shortDelayTime);
        robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
        robot.keyPress(KeyEvent.VK_DELETE);
        robot.delay(normalDelayTime);

        // Input url
        String url = "http://erp.test.com:8008";
        sendKeysByClipBoard(robot, url);   
        robot.keyPress(KeyEvent.VK_ENTER);
        robot.delay(normalDelayTime);

        // Input username for login
        String username = "test";
        sendKeys(robot, username);
        robot.keyPress(KeyEvent.VK_TAB);
        robot.keyPress(KeyEvent.VK_ENTER);
        robot.delay(normalDelayTime);

        // Go to menu SC_OM_SUPERUSER
        robot.mouseMove(100, 540);
        // double click
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.delay(middleDelayTime);
        robot.mouseMove(100, 550);
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.delay(largeDelayTime);

        // Select organization
        robot.mouseMove(100, 420);
        // click then double click
        robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
        robot.delay(middleDelayTime);
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mousePress(MouseEvent.BUTTON1_DOWN_MASK);
        robot.mouseRelease(MouseEvent.BUTTON1_DOWN_MASK);
        robot.delay(normalDelayTime);


        // Call procedure execute some database operation
                
        // ....
    }
}
```

