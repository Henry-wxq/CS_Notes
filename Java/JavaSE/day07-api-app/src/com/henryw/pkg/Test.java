package com.henryw.pkg;

/**
 * 1. 同一个包下的程序，可以直接访问
 * 2. 访问其它包下的程序，必须导包才可以访问
 * 自动导包：settings - auto import - add unambiguous imports on the fly
 * 3. 自己的程序中调用Java提供的程序，也需要先导包才可以使用；注意，Java.lang包下的程序时不需要我们导包的，可以直接使用 e.g. String
 * 4. 访问多个包下的程序，这些程序名又一样的情况下，默认只能导入一个程序，另一个程序必须带包名和类名来访问
 */

public class Test {
}
