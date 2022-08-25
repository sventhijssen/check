module misex1 (
    x0, x1, x2, x3, x4, x5, x6, x7,
    f0, f1, f2, f3, f4, f5, f6  );
  input  x0, x1, x2, x3, x4, x5, x6, x7;
  output f0, f1, f2, f3, f4, f5, f6;
  assign f0 = x2 & (x0 ? (~x1 & ~x3) : (x1 & x3));
  assign f1 = (~x1 & ((x3 & (x0 ^ x2)) | (x5 & ~x0 & x2))) | (~x0 & ~x2 & (x1 | (x6 & ~x3)));
  assign f2 = (x3 & ((~x0 & x1) | (~x2 & x0 & ~x1))) | (~x0 & ((~x3 & ~x1 & (x2 ? ~x5 : ~x6)) | (x4 & ~x2 & x1)));
  assign f3 = (~x0 & ~x2 & x1 & (~x7 | (~x4 & ~x3))) | (~x3 & x2 & ~x1 & (~x5 | x0));
  assign f4 = (~x1 & (x2 ? ~x3 : (x0 & x3))) | (~x0 & (x3 ? (x1 | x2) : ~x2));
  assign f5 = (~x1 & ((x0 & (x3 ^ x2)) | (x5 & ~x3 & x2))) | (~x0 & (x2 ? x3 : (x1 | (x6 & ~x3))));
  assign f6 = (~x1 & ((x0 & (x3 ^ x2)) | (~x5 & ~x3 & x2))) | (~x0 & x1 & (x3 | (~x4 & ~x2)));
endmodule


