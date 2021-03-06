#!/usr/bin/env python

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'longjmp3', """
# DURATION    TID     FUNCTION
   1.164 us [ 4107] | __monstartup();
   0.657 us [ 4107] | __cxa_atexit();
            [ 4107] | main() {
            [ 4107] |   set() {
   0.705 us [ 4107] |     _setjmp() = 0;
   2.065 us [ 4107] |   } /* set */
   1.823 us [ 4107] |   getpid();
            [ 4107] |   set() {
   0.182 us [ 4107] |     _setjmp() = 0;
   0.671 us [ 4107] |   } /* set */
            [ 4107] |   foo() {
            [ 4107] |     __longjmp_chk(1) {
   8.790 us [ 4107] |     } = 1; /* _setjmp */
   9.397 us [ 4107] |   } /* set */
   0.540 us [ 4107] |   getpid();
            [ 4107] |   bar() {
            [ 4107] |     baz() {
            [ 4107] |       __longjmp_chk(2) {
   1.282 us [ 4107] |     } = 2; /* _setjmp */
   1.633 us [ 4107] |   } /* set */
   0.540 us [ 4107] |   getpid();
            [ 4107] |   foo() {
            [ 4107] |     __longjmp_chk(3) {
   0.578 us [ 4107] |     } = 3; /* _setjmp */
   0.949 us [ 4107] |   } /* set */
            [ 4107] |   bar() {
            [ 4107] |     baz() {
            [ 4107] |       __longjmp_chk(4) {
   0.642 us [ 4107] |     } = 4; /* _setjmp */
   0.904 us [ 4107] |   } /* set */
  18.019 us [ 4107] | } /* main */
""")

    def build(self, name, cflags='', ldflags=''):
        return TestBase.build(self, name, cflags + ' -D_FORTIFY_SOURCE=2', ldflags)

    def runcmd(self):
        args = '-A .?longjmp@arg2 -R .?setjmp@retval'
        return '%s %s %s' % (TestBase.ftrace, args, 't-' + self.name)

    def fixup(self, cflags, result):
        return result.replace('__longjmp_chk', "longjmp")
