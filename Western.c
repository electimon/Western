#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main() {
  char command[11111] = "cd resources/bin/ && python Western.py";
  system(command);
}
