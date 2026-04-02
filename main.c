int num = 10;
int *ptr = &num; // & 是取地址符，ptr 存储了 num 的地址

printf("num 的值: %d\n", num);     // 输出: 10
printf("num 的地址: %p\n", &num);  // 输出: num的内存地址
printf("ptr 的值: %p\n", ptr);     // 输出: num的内存地址
printf("ptr 指向的值: %d\n", *ptr);// * 是解引用符，输出: 10