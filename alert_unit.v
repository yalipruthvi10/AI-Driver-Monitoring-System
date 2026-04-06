module alert_unit(
    input drowsy,
    input alcohol,
    output alert
);

assign alert = drowsy | alcohol;

endmodule