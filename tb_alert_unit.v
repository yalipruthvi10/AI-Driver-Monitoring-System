`timescale 1ns/1ps

module tb_alert_unit;

reg drowsy, alcohol;
wire alert;

alert_unit uut(.drowsy(drowsy), .alcohol(alcohol), .alert(alert));

initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0, tb_alert_unit);

    drowsy = 0; alcohol = 0;
    #10 drowsy = 1;
    #10 alcohol = 1;
    #10 drowsy = 0;
    #10 alcohol = 0;

    #10 $finish;
end

endmodule