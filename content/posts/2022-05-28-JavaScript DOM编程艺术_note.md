---
title: JavaScript DOM编程艺术_note
date: 2022-05-28
---

***
<div style="float:left">18 第 1 章　JavaScript简史</div><div style="float:right">Aug 06, 2021</div>

> Netscape Navigator 4发布于1997年6月，IE 4发布于同年10月。这两种浏览器都对它们的早期版本进
行了许多改进，大幅扩展了DOM，使能够通过JavaScript完成的功能大大增加。而网页设计人员也开始
接触到一个新名词：DHTML。

原来我之前用的水平还停留再97年

***
<div style="float:left">46 第 2 章　JavaScript语法</div><div style="float:right">Aug 07, 2021</div>

> 如果在某个函数中使用了var，那个变量就将被视为一个局部变量，
反之，如果没有使用var，那个变量就将被视为一个全局变量，如果


***
<div style="float:left">53 第 3 章　DOM</div><div style="float:right">Aug 07, 2021</div>

> 宿主对象（host object）：由浏览器提供的对象。


***
<div style="float:left">54 第 3 章　DOM</div><div style="float:right">Aug 07, 2021</div>

> DOM把文档表示为一棵家谱树。

js中的model表示的是结构模型

***
<div style="float:left">67 第 3 章　DOM</div><div style="float:right">Aug 09, 2021</div>

> 这里有一个非常值得关注的细节：通过setAttribute对文档做出修改后，在通过浏览器的view
source（查看源代码）选项去查看文档的源代码时看到的仍将是改变前的属性值，也就是说，
setAttribute做出的修改不会反映在文档本身的源代码里。这种“表里不一”的现象源自DOM的工作
模式：先加载文档的静态内容，再动态刷新，动态刷新不影响文档的静态内容。这正是DOM的真正威
力：对页面内容进行刷新却不需要在浏览器里刷新页面。


***
<div style="float:left">76 第 4 章　案例研究：JavaScript图片库</div><div style="float:right">Aug 09, 2021</div>

> 当点击这个链接时，因为onclick事件处理函数所触发的JavaScript代码返回给它的值是false，所以
这个链接的默认行为没有被触发。


***
<div style="float:left">96 第 5 章　最佳实践</div><div style="float:right">Aug 09, 2021</div>

> 部</body>之前，就不能保证哪个文件最先结束加载（浏览器可能一次加载多个）。因为脚本加载时文
档可能不完整，所以模型也不完整。没有完整的DOM，getElementsByTagName等方法就不能正常工
作。


***
<div style="float:left">97 第 5 章　最佳实践</div><div style="float:right">Aug 09, 2021</div>

> 前先检查用户所使用的浏览器是否支持这个方法。在使用对象检测时，一定要删掉方法名后面的圆括
号，如果不删掉，测试的将是方法的结果，无论方法是否存在。


***
<div style="float:left">108 第 6 章　案例研究：图片库改进版</div><div style="float:right">Aug 11, 2021</div>

> 这项测试是一个预防性措施。现在我知道调用这个JavaScript函数的文档里有一个id属性值等于
imagegallery的列表清单元素，但我不敢确定这在将来会不会发生变化。有了这个预防性措施，
即使以后我决定从网页上删掉图片库，也用不着担心这个网页的JavaScript代码会突然出错。把
HTML文档的内容与JavaScript代码所实现的行为分离开来的重要性由此可见一斑。作为一条原则，


***
<div style="float:left">108 第 6 章　案例研究：图片库改进版</div><div style="float:right">Aug 11, 2021</div>

> 我个人认为，如果一个函数有多个出口，只要这些出口集中出现在函数的开头部分，就是可以
接受的。
出于可读性的考虑，我把那些return false语句全部集中到prepareGallery的开头部分：
function prepareGallery() { 
  if (!document.getElementsByTagName) return false; 
  if (!document.getElementById) return false; 
if (!document.getElementById("imagegallery")) return false;
必要的测试和检查工作就绪之后，我现在开始写事件处理函数的核心功能。


***
<div style="float:left">114 第 6 章　案例研究：图片库改进版</div><div style="float:right">Aug 11, 2021</div>

> var description = document.getElementById("description"); 
description.firstChild.nodeValue = text; 

修改元素节点中的文字节点的做法

***
<div style="float:left">133 第 7 章　动态创建标记</div><div style="float:right">Aug 13, 2021</div>

> XHTML文档）

是xml风格的html，更为严谨，所有标签必须关闭，如</a>

***
<div style="float:left">152 第 7 章　动态创建标记</div><div style="float:right">Aug 16, 2021</div>

> 注意　在为onreadystatechange指定函数引用时，不要在函数名后面加括号。因为加括号表示
立即调用函数，而我们在此只想把函数自身的引用（而不是函数结果）赋值给onreadystate-
change属性。


***
<div style="float:left">173 第 8 章　充实文档的内容</div><div style="float:right">Aug 30, 2021</div>

> 核心内容。缩略语列表是一种很好的增强补充，它还算不上是页面必不可少的组成部分。如果它真的必
不可少，从一开始就应该把它包括在标记里。


***
<div style="float:left">183 第 8 章　充实文档的内容</div><div style="float:right">Aug 30, 2021</div>

> 希望大家始终记住：JavaScript脚本只应该用来充实文档的内容，要避免使用DOM技术来创建核心内
容。


***
<div style="float:left">194 第 9 章　CSS-DOM</div><div style="float:right">Sep 01, 2021</div>

> style属性只能返回内嵌样式。换句话说，只有把CSS style属性插入到标记里，才可以用DOM style
属性去查询那些信息：


***
<div style="float:left">198 第 9 章　CSS-DOM</div><div style="float:right">Sep 01, 2021</div>

> 现在，CSS还无法根据元素之间的相对位置关系找出某个特定的元素，但这对DOM来说却不是什么难题。


***
<div style="float:left">209 第 9 章　CSS-DOM</div><div style="float:right">Sep 02, 2021</div>

> 如果对包含以上标记的文档使用styleHeaderSiblings函数，那个“文本段”元素的class属性将
从disclaimer被替换为intro，而这里实际需要的是“追加”效果——class属性应该变成
disclaimer intro，也就是disclaimer和intro两种样式的叠加。

用js修改class，只追加不覆盖

***
<div style="float:left">212 第 9 章　CSS-DOM</div><div style="float:right">Sep 08, 2021</div>

> HTML-DOM。

是html的对象模型，提供给js的编程接口。有一些和dom core不同的方法。如element.value=

***
