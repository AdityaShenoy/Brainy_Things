s = '''☺Rimport☺ ☺Bjava☺☺W.☺☺Butil☺☺W.☺☺R*☺☺W;☺

☺Rpublic☺ ☺Bclass ☺GBrainyThings☺ {
  ☺Rpublic☺ ☺Rstatic☺ ☺Bvoid☺ ☺Gmain☺(☺BString☺☺R[]☺ ☺Oargs☺) {
    ☺BInteger☺☺R[]☺ ☺Wa☺ ☺R=☺ {☺P1☺, ☺P4☺, ☺P2☺, ☺P3☺, ☺P5☺};
    
    ☺BList☺☺W<☺☺BInteger☺☺W>☺ ☺Wl☺ = ☺BArrays☺.☺BasList☺(a);
    ☺BSystem☺.out.☺Bprintln☺(l);
    ☺BSystem☺.out.☺Bprintln☺(☺BArrays☺.☺BtoString☺(a));

    l.☺Bset☺(☺P2☺, ☺P8☺);
    ☺BSystem☺.out.☺Bprintln☺(l);
    ☺BSystem☺.out.☺Bprintln☺(☺BArrays☺.☺BtoString☺(a));
  }
}'''

# f('#a366ff', purple)
# f('#ff002b', red)
# f('#0099cc', blue)
# f('#77b300', green)
# f('#ff9900', orange)
s = s.replace(' ', '&nbsp;')
s = s.replace('<', '&lt;')
s = s.replace('>', '&gt;')
s = s.replace('\n', '<br />')
s = s.replace('☺B', '<span style="color:#0099cc;">')
s = s.replace('☺G', '<span style="color:#77b300;">')
s = s.replace('☺O', '<span style="color:#ff9900;">')
s = s.replace('☺P', '<span style="color:#a366ff;">')
s = s.replace('☺R', '<span style="color:#ff002b;">')
s = s.replace('☺', '</span>')
print(s)