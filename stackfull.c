#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Robert W. Oliver II");
MODULE_DESCRIPTION("A simple example Linux module.");
MODULE_VERSION("0.01");

static int mymodule_add_recursion(int n)
{
    int r = 2;
    int a = 5;
    int b = 6;
    int c = 7;
    int d = 8;
    int e = 9;

    printk(KERN_INFO "---n-[%d]\n", n);

    r = a + b + c + d + e + n; 
    if (n > 0) {
        r += mymodule_add_recursion(n-1);
    }

    printk(KERN_INFO "===r=[%d]\n", r);

    return r;
}

static int __init mymodule_stackfull_init(void) 
{
    int r;

    printk(KERN_INFO "Hello, World!\n");

    r = mymodule_add_recursion(450);

    printk(KERN_INFO "main: [%d]\n", r);

    return 0;
}

static void __exit mymodule_stackfull_exit(void) 
{
    printk(KERN_INFO "Goodbye, World!\n");
}

module_init(mymodule_stackfull_init);
module_exit(mymodule_stackfull_exit);

/*

==== /sys/kernel/debug/tracing/stack_max_size
15592


==== /sys/kernel/debug/tracing/stack_trace
        Depth    Size   Location    (461 entries)
        -----    ----   --------
  0)    15592     144   vt_console_print+0x7f/0x430
  1)    15448      64   console_unlock+0x468/0x4b0
  2)    15384     112   vprintk_emit+0x3c4/0x510
  3)    15272      16   vprintk_default+0x29/0x40
  4)    15256      96   printk+0x60/0x77
  5)    15160      32   mymodule_add_recursion+0x22/0x4a [stackfull]
  6)    15128      32   mymodule_add_recursion+0x2e/0x4a [stackfull]
  7)    15096      32   mymodule_add_recursion+0x2e/0x4a [stackfull]
  8)    15064      32   mymodule_add_recursion+0x2e/0x4a [stackfull]

*/

/*
obj-m += stackfull.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

*/
