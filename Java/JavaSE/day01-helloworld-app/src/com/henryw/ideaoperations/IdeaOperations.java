package com.henryw.ideaoperations;

/**
 * IDEA中的其他操作
 * 1. 删除类文件：右键Javaclass - Delete
 * 2. 修改类名称：右键 - Refactor
 * 3. 修改模块名：右键 - Rnefactor - reame - rename module and directory(工程里名字也同步更改；右键-openin-explorer快速查看)
 * 4. 导入模块：
 *      1) 关联导入(模块路径不在工程下)：找到模块位置，拷贝路径 - IDEA - File - New - Module from existing Sources - 粘贴路径
 *      - 点 .iml文件进行导入 - OK
 *      2) 复制导入(推荐)：先将模块复制到工程里面 - 拷贝路径 - IDEA - File - New - Module from existing Sources - 粘贴路径
 *      - 点 .iml文件进行导入 - OK
 *      3) IDEA - File - New - Module; 将模块内src文件夹下的文件全部复制到新的模块下的src文件夹内(在IDEA内粘贴)
 * 5. 删除模块: IDEA - 右键模块 - Remove Module；进入磁盘内，在工程里在进行一次删除；一定要先在IDEA内删除，再去工程里删除
 * 6. 打开工程：工程自带iml，所以可以直接在file - open - 选择即可
 * 7. 关闭工程：file - close project
 */

public class IdeaOperations {
}
