#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(){
    int fd, src, dst, n, total = 0;
    char text[] = "Hello from POSIX file I/O!\n";
    char buf[100];

    fd = open("demo.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);      // create file
    if (fd < 0) {
        printf("cannot open file\n");
        return 1;
    }
    printf("File descriptor: %d\n", fd);
    write(fd, text, strlen(text));      // write text
    close(fd);

    fd = open("demo.txt", O_RDONLY);
    n = read(fd, buf, 99);      // read back
    buf[n] = '\0';
    printf("Read %d bytes: %s", n, buf);
    close(fd);

    src = open("demo.txt", O_RDONLY);
    dst = open("demo_copy.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    while ((n = read(src, buf, 10)) > 0) {      // copy chunks
        write(dst, buf, n);
        total = total + n;
    }
    close(src);
    close(dst);
    printf("Copied %d bytes\n", total);
    return 0;
}
