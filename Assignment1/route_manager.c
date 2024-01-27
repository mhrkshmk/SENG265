/** @file route_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process airline routes.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author STUDENT_NAME
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */

struct flightInformation {
    /*
        This struct resembles the structure of the flight information.
    */
    char airline_name[100], airline_icao_unique_code[100], airline_country[100], from_airport_name[100], from_airport_city[100], from_airport_country[100], from_airport_icao_unique_code[100], to_airport_name[100], to_airport_city[100], to_airport_country[100], to_airport_icao_unique_code[100];
    char from_airport_altitude[100], to_airport_altitude[100];
} Flights[100000] ;

void fixInput(char data[]) {
    /*
        This function fixes the inputs given, by removing the extra characters from it.

            Parameters
            ----------
                char data[]
                    the array that needs to be fixed.

            Returns
            -------
                Nothing.
    */
    int ind = 0, cnt = 0;
    char array[100];
    for (int i = 0; i < strlen(data); i++) {
        char c = data[i];
        if (c == '=') {
            ind = i + 1;
            break;
        }
    }
    for (int i = ind; i < strlen(data); i++) {
        char c = data[i];
        array[cnt++] = c;
    }
    array[cnt] = '\0';
    strcpy(data, array);
}

void addData(char data[], int ind) {
    /*
        This function gets a line of data from csv table, and add its corresponding values to the struct of flight informations.

            Parameters
            ----------
                char data[]
                    A string that is a line from the csv data table.
                int ind
                    An index telling how many flights have been added up to now and which index should the next flight information be added to.

            Returns
            -------
                Nothing
    */
    char* val = strtok(data, ",");
    int col = 0;
    while (val) {
        if (col == 0)
            strcpy(Flights[ind].airline_name, val);
        if (col == 1)
            strcpy(Flights[ind].airline_icao_unique_code, val);
        if (col == 2)
            strcpy(Flights[ind].airline_country,val);
        if (col == 3)
            strcpy(Flights[ind].from_airport_name, val);
        if (col == 4)
            strcpy(Flights[ind].from_airport_city, val);
        if (col == 5)
            strcpy(Flights[ind].from_airport_country, val);
        if (col == 6)
            strcpy(Flights[ind].from_airport_icao_unique_code, val);
        if (col == 7)
            strcpy(Flights[ind].from_airport_altitude, val);
        if (col == 8)
            strcpy(Flights[ind].to_airport_name, val);
        if (col == 9)
            strcpy(Flights[ind].to_airport_city, val);
        if (col == 10)
            strcpy(Flights[ind].to_airport_country, val); 
        if (col == 11)
            strcpy(Flights[ind].to_airport_icao_unique_code, val);
        if (col == 12)
            strcpy(Flights[ind].to_airport_altitude, val);
        val = strtok(NULL, ",");
        col ++;
    }
}

int readFileInfo(char filename[]) {
    /*
        This function reads the data lines from the file, and fixes each line so that the empty table cells won't distrupt the information processing, and returns the number of rows in that csv table.

            Parameters
            ----------
                char filename[]
                    The file name that needs to be processed.

            Returns
            -------
                int
                    The number of Rows(Flights) in the file.
    */
    FILE* fp = fopen(filename, "r");
    char line[10000];
    int cnt = 0, flight_count = 0;
    while (fgets(line, 1000, fp)) {
        if (cnt == 0) {
            cnt ++;
            continue;
        }
        char full_data[10000] = "";
        if (line[0] == ',') {
            strncat(full_data, "NaN", 3);
        }
        for (int i = 0; i < strlen(line) - 1; i ++) {
            char c = line[i];
            strncat(full_data, &c, 1);
            if (line[i] == line[i + 1] && line[i] == ',')
                strncat(full_data, "NaN", 3);
        }
        char c = line[strlen(line) - 2];
        if (c == ',')
            strncat(full_data, "NaN", 3);
        addData(full_data, flight_count);
        flight_count++;
    }
    return flight_count;
    fclose(fp);
}

void printOutputTypeOne(char airline[], char dest_country[], int flight_count) {
    /*
        This function prints the matched flights in a file for input type ONE.

            Parameters
            ----------
                char airline[]
                    The airline name or icao given in the input.
                char dest_country[]
                    The destination country given in the input.
                int flight_count
                    The number of flights in the table.

            Returns
            -------
                Nothing.
    */
    FILE* fp = fopen("output.txt", "w");
    bool any_flight = false;
    char airline_name[1000], airline_icao[100];
    for (int i = 0; i < flight_count; i++) {
        if (strstr(Flights[i].to_airport_country, dest_country) != NULL && (strstr(Flights[i].airline_icao_unique_code, airline) != NULL || strstr(Flights[i].airline_name, airline) != NULL)) {
            strcpy(airline_name, Flights[i].airline_name);
            strcpy(airline_icao, Flights[i].airline_icao_unique_code);
            any_flight = true;
            break;
        }
    }
    if (!any_flight) {
        fprintf(fp, "NO RESULTS FOUND.\n");
        return;
    }
    fprintf(fp, "FLIGHTS TO %s BY %s (%s):\n", dest_country, airline_name, airline_icao);
    for (int i = 0; i < flight_count; i++) {
        if (strstr(Flights[i].to_airport_country, dest_country) != NULL && (strstr(Flights[i].airline_icao_unique_code, airline) != NULL || strstr(Flights[i].airline_name, airline) != NULL)) {
                fprintf(fp, "FROM: %s, %s, %s TO: %s (%s), %s\n", Flights[i].from_airport_icao_unique_code, Flights[i].from_airport_city, Flights[i].from_airport_country, Flights[i].to_airport_name, Flights[i].to_airport_icao_unique_code, Flights[i].to_airport_city);
        }
    }
    fclose(fp);
}

void printOutputTypeTwo(char src_country[], char dest_city[], char dest_country[], int flight_count) {
    /*
        This function prints the matched flights in a file for input type TWO.

            Parameters
            ----------
                char src_country[]
                    The source country given in the input.
                char dest_city[]
                    The destination city given in the input.
                char dest_country[]
                    The destination country given in the input.
                int flight_count
                    The number of flights in the table.

            Returns
            -------
                Nothing.
    */

    FILE* fp = fopen("output.txt", "w");
    bool any_flight = false;
    for (int i = 0; i < flight_count; i++)
        if (strstr(Flights[i].from_airport_country, src_country) != NULL && strstr(Flights[i].to_airport_city, dest_city) != NULL && strstr(Flights[i].to_airport_country, dest_country) != NULL) {
            any_flight = true;
            fprintf(fp, "FLIGHTS FROM %s TO %s, %s:\n", Flights[i].from_airport_country, Flights[i].to_airport_city, Flights[i].to_airport_country);
            break;
        }
    if (!any_flight) {
        fprintf(fp, "NO RESULTS FOUND.\n");
        return;
    }
    for (int i = 0; i < flight_count; i++)
        if (strstr(Flights[i].from_airport_country, src_country) != NULL && strstr(Flights[i].to_airport_city, dest_city) != NULL && strstr(Flights[i].to_airport_country, dest_country) != NULL) {
            fprintf(fp, "AIRLINE: %s (%s) ORIGIN: %s (%s), %s\n", Flights[i].airline_name, Flights[i].airline_icao_unique_code, Flights[i].from_airport_name, Flights[i].from_airport_icao_unique_code, Flights[i].from_airport_city);
        }
    fclose(fp);
}

void printOutputTypeThree(char src_city[], char src_country[], char dest_city[], char dest_country[], int flight_number) {
    /*
        This function prints the matched flights in a file for input type TWO.

            Parameters
            ----------
                char src_city[]
                    The source city given in the input.
                char src_country[]
                    The source country given in the input.
                char dest_city[]
                    The destination city given in the input.
                char dest_country[]
                    The destination country given in the input.
                int flight_count
                    The number of flights in the table.

            Returns
            -------
                Nothing.
    */

    FILE* fp = fopen("output.txt", "w");
    bool any_flight = false;
    for (int i = 0; i < flight_number; i++)
        if (strstr(Flights[i].from_airport_city, src_city) != NULL && strstr(Flights[i].from_airport_country, src_country) != NULL && strstr(Flights[i].to_airport_city, dest_city) != NULL && strstr(Flights[i].to_airport_country, dest_country) != NULL) {
            fprintf(fp, "FLIGHTS FROM %s, %s TO %s, %s:\n", src_city, src_country, dest_city, dest_country);
            any_flight = true;
            break;
        }
    if (!any_flight) {
        fprintf(fp, "NO RESULTS FOUND.\n");
        return;
    }
    for (int i = 0; i < flight_number; i++)
        if (strstr(Flights[i].from_airport_city, src_city) != NULL && strstr(Flights[i].from_airport_country, src_country) != NULL && strstr(Flights[i].to_airport_city, dest_city) != NULL && strstr(Flights[i].to_airport_country, dest_country) != NULL)
            fprintf(fp, "AIRLINE: %s (%s) ROUTE: %s-%s\n", Flights[i].airline_name, Flights[i].airline_icao_unique_code, Flights[i].from_airport_icao_unique_code, Flights[i].to_airport_icao_unique_code);
    fclose(fp);
}

int main(int argc, char *argv[]) {
    // TODO: your code.
    for (int i = 1; i < argc; i++) {
        fixInput(argv[i]);
    }
    int flight_count = 0;
    if (argc == 4) {
        /*
            This if statement fixes The input if it is of type 1, by seperating the input to different values and fixing each value by using the fixInput function.
            Then it calls another function to print the results in another file.
        */
        flight_count = readFileInfo(argv[1]);
        printOutputTypeOne(argv[2], argv[3], flight_count);

    }
    else if (argc == 5) {
        /*
            This if statement fixes The input if it is of type 2, by seperating the input to different values and fixing each value by using the fixInput function.
            Then it calls another function to print the results in another file.
        */
        flight_count = readFileInfo(argv[1]);
        printOutputTypeTwo(argv[2], argv[3], argv[4], flight_count);
    }
    else if (argc == 6) {
        /*
            This if statement fixes The input if it is of type 3, by seperating the input to different values and fixing each value by using the fixInput function.
            Then it calls another function to print the results in another file.
        */
        flight_count = readFileInfo(argv[1]);
        printOutputTypeThree(argv[2], argv[3], argv[4], argv[5], flight_count);
    }
}

