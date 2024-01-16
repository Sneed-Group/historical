unsigned char inport(wchar_t keyid, wchar_t state) {
  return inportb(keyid); //super hacky way to inport
}

unsigned char outport(wchar_t scancode, wchar_t state) {
  return (outport(scancode, state)); //hacky way to set key state.
}


void kbd_ack(void){
  while(!(inport(0x60, 0xfa)==0xfa));
}


void kbd_led_handling(wchar_t ledstatus){;
  outport(0x60,0xed);
  kbd_ack();
  outport(0x60,ledstatus);
}
