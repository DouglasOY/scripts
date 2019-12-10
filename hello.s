
hello:     file format elf64-x86-64

000000000040051d <sum_eight>:
#include <stdio.h>

long sum_eight(long a, long b, long c, long d, long e, long f, long g, long h)
{
  40051d:	55                   	push   %rbp
  40051e:	48 89 e5             	mov    %rsp,%rbp
  400521:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
  400525:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
  400529:	48 89 55 d8          	mov    %rdx,-0x28(%rbp)
  40052d:	48 89 4d d0          	mov    %rcx,-0x30(%rbp)
  400531:	4c 89 45 c8          	mov    %r8,-0x38(%rbp)
  400535:	4c 89 4d c0          	mov    %r9,-0x40(%rbp)
    long ret = 67;
  400539:	48 c7 45 f8 43 00 00 	movq   $0x43,-0x8(%rbp)
  400540:	00 
    ret = a+b+c+d+e+f+g+h;
  400541:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
  400545:	48 8b 55 e8          	mov    -0x18(%rbp),%rdx
  400549:	48 01 c2             	add    %rax,%rdx
  40054c:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
  400550:	48 01 c2             	add    %rax,%rdx
  400553:	48 8b 45 d0          	mov    -0x30(%rbp),%rax
  400557:	48 01 c2             	add    %rax,%rdx
  40055a:	48 8b 45 c8          	mov    -0x38(%rbp),%rax
  40055e:	48 01 c2             	add    %rax,%rdx
  400561:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
  400565:	48 01 c2             	add    %rax,%rdx
  400568:	48 8b 45 10          	mov    0x10(%rbp),%rax
  40056c:	48 01 c2             	add    %rax,%rdx
  40056f:	48 8b 45 18          	mov    0x18(%rbp),%rax
  400573:	48 01 d0             	add    %rdx,%rax
  400576:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    return ret;
  40057a:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
}
  40057e:	5d                   	pop    %rbp
  40057f:	c3                   	retq   

0000000000400580 <sum_two>:

long sum_two(long first, long second)
{
  400580:	55                   	push   %rbp
  400581:	48 89 e5             	mov    %rsp,%rbp
  400584:	48 83 ec 70          	sub    $0x70,%rsp
  400588:	48 89 7d a8          	mov    %rdi,-0x58(%rbp)
  40058c:	48 89 75 a0          	mov    %rsi,-0x60(%rbp)
    long sum = 66;
  400590:	48 c7 45 f8 42 00 00 	movq   $0x42,-0x8(%rbp)
  400597:	00 
    long a = 33;
  400598:	48 c7 45 f0 21 00 00 	movq   $0x21,-0x10(%rbp)
  40059f:	00 
    long b = 34;
  4005a0:	48 c7 45 e8 22 00 00 	movq   $0x22,-0x18(%rbp)
  4005a7:	00 
    long c = 35;
  4005a8:	48 c7 45 e0 23 00 00 	movq   $0x23,-0x20(%rbp)
  4005af:	00 
    long d = 36;
  4005b0:	48 c7 45 d8 24 00 00 	movq   $0x24,-0x28(%rbp)
  4005b7:	00 
    long e = 37;
  4005b8:	48 c7 45 d0 25 00 00 	movq   $0x25,-0x30(%rbp)
  4005bf:	00 
    long f = 38;
  4005c0:	48 c7 45 c8 26 00 00 	movq   $0x26,-0x38(%rbp)
  4005c7:	00 
    long g = 39;
  4005c8:	48 c7 45 c0 27 00 00 	movq   $0x27,-0x40(%rbp)
  4005cf:	00 
    long h = 40;
  4005d0:	48 c7 45 b8 28 00 00 	movq   $0x28,-0x48(%rbp)
  4005d7:	00 
    
    sum = first + second;
  4005d8:	48 8b 45 a0          	mov    -0x60(%rbp),%rax
  4005dc:	48 8b 55 a8          	mov    -0x58(%rbp),%rdx
  4005e0:	48 01 d0             	add    %rdx,%rax
  4005e3:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    printf("first_second==[%ld]\n", sum);
  4005e7:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  4005eb:	48 89 c6             	mov    %rax,%rsi
  4005ee:	bf 20 07 40 00       	mov    $0x400720,%edi
  4005f3:	b8 00 00 00 00       	mov    $0x0,%eax
  4005f8:	e8 03 fe ff ff       	callq  400400 <printf@plt>

    sum += sum_eight(a, b, c, d, e, f, g, h);
  4005fd:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
  400601:	4c 8b 45 d0          	mov    -0x30(%rbp),%r8
  400605:	48 8b 4d d8          	mov    -0x28(%rbp),%rcx
  400609:	48 8b 55 e0          	mov    -0x20(%rbp),%rdx
  40060d:	48 8b 75 e8          	mov    -0x18(%rbp),%rsi
  400611:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  400615:	48 8b 7d b8          	mov    -0x48(%rbp),%rdi
  400619:	48 89 7c 24 08       	mov    %rdi,0x8(%rsp)
  40061e:	48 8b 7d c0          	mov    -0x40(%rbp),%rdi
  400622:	48 89 3c 24          	mov    %rdi,(%rsp)
  400626:	48 89 c7             	mov    %rax,%rdi
  400629:	e8 ef fe ff ff       	callq  40051d <sum_eight>
  40062e:	48 01 45 f8          	add    %rax,-0x8(%rbp)
    return sum;
  400632:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
}
  400636:	c9                   	leaveq 
  400637:	c3                   	retq   

0000000000400638 <main>:

int main(void)
{
  400638:	55                   	push   %rbp
  400639:	48 89 e5             	mov    %rsp,%rbp
  40063c:	48 83 ec 20          	sub    $0x20,%rsp
    long ret = 65;
  400640:	48 c7 45 f8 41 00 00 	movq   $0x41,-0x8(%rbp)
  400647:	00 
    long first = 4;
  400648:	48 c7 45 f0 04 00 00 	movq   $0x4,-0x10(%rbp)
  40064f:	00 
    long second = 5;
  400650:	48 c7 45 e8 05 00 00 	movq   $0x5,-0x18(%rbp)
  400657:	00 

    ret = sum_two(first, second);
  400658:	48 8b 55 e8          	mov    -0x18(%rbp),%rdx
  40065c:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  400660:	48 89 d6             	mov    %rdx,%rsi
  400663:	48 89 c7             	mov    %rax,%rdi
  400666:	e8 15 ff ff ff       	callq  400580 <sum_two>
  40066b:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    printf("main==[%ld]\n", ret);
  40066f:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  400673:	48 89 c6             	mov    %rax,%rsi
  400676:	bf 35 07 40 00       	mov    $0x400735,%edi
  40067b:	b8 00 00 00 00       	mov    $0x0,%eax
  400680:	e8 7b fd ff ff       	callq  400400 <printf@plt>

    return 0;
  400685:	b8 00 00 00 00       	mov    $0x0,%eax
}
  40068a:	c9                   	leaveq 
  40068b:	c3                   	retq   
  40068c:	0f 1f 40 00          	nopl   0x0(%rax)


(gdb) info reg
rax            0x21 33
rbx            0x0  0
rcx            0x24 36
rdx            0x23 35
rsi            0x22 34
rdi            0x21 33
rbp            0x7fffffffe1a0   0x7fffffffe1a0
rsp            0x7fffffffe1a0   0x7fffffffe1a0
r8             0x25 37
r9             0x26 38
r10            0x22 34
r11            0x246    582
r12            0x400430 4195376
r13            0x7fffffffe330   140737488347952
r14            0x0  0
r15            0x0  0
rip            0x400541 0x400541 <sum_eight+36>
eflags         0x202    [ IF ]
cs             0x33 51
ss             0x2b 43
ds             0x0  0
es             0x0  0
fs             0x0  0
gs             0x0  0

(gdb) x /100x 0x7fffffffe150
0x7fffffffe150: 0x00000000  0x00000000  0x00000000  0x00000000
0x7fffffffe160: 0x00000026  0x00000000  0x00000025  0x00000000
0x7fffffffe170: 0x00000024  0x00000000  0x00000023  0x00000000
0x7fffffffe180: 0x00000022  0x00000000  0x00000021  0x00000000
0x7fffffffe190: 0x00000000  0x00000000  0x00000043  0x00000000
0x7fffffffe1a0: 0xffffe220  0x00007fff  0x0040062e  0x00000000
0x7fffffffe1b0: 0x00000027  0x00000000  0x00000028  0x00000000
0x7fffffffe1c0: 0x00000005  0x00000000  0x00000004  0x00000000
0x7fffffffe1d0: 0x00000000  0x00000000  0x00000028  0x00000000
0x7fffffffe1e0: 0x00000027  0x00000000  0x00000026  0x00000000
0x7fffffffe1f0: 0x00000025  0x00000000  0x00000024  0x00000000
0x7fffffffe200: 0x00000023  0x00000000  0x00000022  0x00000000
0x7fffffffe210: 0x00000021  0x00000000  0x00000009  0x00000000
0x7fffffffe220: 0xffffe250  0x00007fff  0x0040066b  0x00000000
0x7fffffffe230: 0x00400690  0x00000000  0x00000005  0x00000000
0x7fffffffe240: 0x00000004  0x00000000  0x00000041  0x00000000
0x7fffffffe250: 0x00000000  0x00000000  0xf7a30445  0x00007fff
0x7fffffffe260: 0x00000000  0x00000000  0xffffe338  0x00007fff
0x7fffffffe270: 0x00000000  0x00000001  0x00400638  0x00000000
0x7fffffffe280: 0x00000000  0x00000000  0x58c969ee  0x7e4fd601
0x7fffffffe290: 0x00400430  0x00000000  0xffffe330  0x00007fff
0x7fffffffe2a0: 0x00000000  0x00000000  0x00000000  0x00000000
0x7fffffffe2b0: 0x9c0969ee  0x81b029fe  0x5f3369ee  0x81b03947
0x7fffffffe2c0: 0x00000000  0x00000000  0x00000000  0x00000000
0x7fffffffe2d0: 0x00000000  0x00000000  0x00000000  0x00000000

(gdb) bt
#0  sum_eight (a=33, b=34, c=35, d=36, e=37, f=38, g=39, h=40) at good.c:6
#1  0x000000000040062e in sum_two (first=4, second=5) at good.c:25
#2  0x000000000040066b in main () at good.c:35

(gdb) info frame 2
Stack frame at 0x7fffffffe260:
 rip = 0x40066b in main (good.c:35); saved rip 0x7ffff7a30445
 caller of frame at 0x7fffffffe230
 source language c.
 Arglist at 0x7fffffffe250, args: 
 Locals at 0x7fffffffe250, Previous frame's sp is 0x7fffffffe260
 Saved registers:
  rbp at 0x7fffffffe250, rip at 0x7fffffffe258

(gdb) info frame 1
Stack frame at 0x7fffffffe230:
 rip = 0x40062e in sum_two (good.c:25); saved rip 0x40066b
 called by frame at 0x7fffffffe260, caller of frame at 0x7fffffffe1b0
 source language c.
 Arglist at 0x7fffffffe220, args: first=4, second=5
 Locals at 0x7fffffffe220, Previous frame's sp is 0x7fffffffe230
 Saved registers:
  rbp at 0x7fffffffe220, rip at 0x7fffffffe228

(gdb) info frame 0
Stack frame at 0x7fffffffe1b0:
 rip = 0x400541 in sum_eight (good.c:6); saved rip 0x40062e
 called by frame at 0x7fffffffe230
 source language c.
 Arglist at 0x7fffffffe1a0, args: a=33, b=34, c=35, d=36, e=37, f=38, g=39, h=40
 Locals at 0x7fffffffe1a0, Previous frame's sp is 0x7fffffffe1b0
 Saved registers:
  rbp at 0x7fffffffe1a0, rip at 0x7fffffffe1a8


