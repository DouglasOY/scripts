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
