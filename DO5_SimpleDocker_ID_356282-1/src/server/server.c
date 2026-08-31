#include <stdlib.h>
#include <fcgi_stdio.h>


int main() {
    while (FCGI_Accept() >= 0) {
        printf("Content-Type: text/html\r\n");
	printf("\r\n");
	printf("<!DOCTYPE html><html><head><title>Hello</title></head><body>");
        printf("<h1>Hello world!</h1>");
        printf("</body></html>");
    }
    return 0;
}
