#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main() {
  char command[11111] = "cd resources/ && python Western.py";
  system(command);
}
