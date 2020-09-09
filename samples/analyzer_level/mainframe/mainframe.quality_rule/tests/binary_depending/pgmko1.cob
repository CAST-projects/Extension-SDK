       IDENTIFICATION DIVISION.
       PROGRAM-ID. PGM1.
       DATA DIVISION.
       01 VARS
         05 TABLE_SIZE PIC 9(4).
         05 MY_TABLE OCCURS 1 TO 10
                        DEPENDING ON TABLE_SIZE
                        PIC X(10).
       PROCEDURE DIVISION.
       STOP RUN.
       
