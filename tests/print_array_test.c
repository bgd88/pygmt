#include <stdio.h>

void multiplyarray(const void * indatav, int rowcount, int colcount, void * outdatav) {
    //void cfun(const double * indata, int rowcount, int colcount, double * outdata) {
    const double * indata = (double *) indatav;
    double * outdata = (double *) outdatav;
    int i;
    puts("Currently Doing stuff lots of important stuff to our array ... ");
    for (i = 0; i < rowcount * colcount; ++i) {
	outdata[i] = indata[i] * 5;
    }
    puts("Like Multiplying by 5");
}
