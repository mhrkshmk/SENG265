/** @file route_manager.c
 *  @brief A small program to analyze airline routes data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author Mehrkish M.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

// TODO: Make sure to adjust this based on the input files given
#define MAX_LINE_LEN 256

/**
 * @brief Serves aas an incremental counter for navigating the list.
 *
 * @param p The pointer of the node to print.
 * @param arg The pointer of the index.
 *
 */

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}

/**
 * @brief Allows to print out the content of a node.
 *
 * @param p The pointer of the node to print.
 * @param arg The format of the string.
 *
 */

void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->word);
}

/**
 * @brief Allows to print each node in the list.
 *
 * @param l The first node in the list
 *
 */

void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);
    printf("Number of words: %d\n", len);

    apply(l, print_node, "%s\n");
}

/**
 * fixInput : This function fixed the input given, by removing the extra characters from it.
 *
 * @param data : The string that needs to be fixed.
 *
 */

void fixInput(char data[]) {
    int ind = 0;
    for (int i = 0; i < strlen(data); i++) {
        char c = data[i];
        if (c == '=') {
            ind = i + 1;
            break;
        }
    }

    char *array = (char *)malloc(sizeof(char) * (strlen(data) - ind));
    for (int i = ind; i < strlen(data); i++) {
        char c = data[i];
        array[i - ind] = c;
    }

    array[strlen(array)] = '\0';
    strcpy(data, array);
}

/**
 * addValue : his function gets the head of a linked list and adds a node to it, by calling the add_end function from the list header. If the value already exists, it adds 1 to its cnt attribute.
 *
 * @param head : A pointer to the head of linked list.
 * @param info : A string for the value of word attribute of the node.
 *
 * @return : A pointer to the head of the new list after changes.
 *
 */


node_t* addValue(node_t *head, char info[]) {
    if (head == NULL)
        return new_node(info);

    node_t *tmp_head = head;
    while (head != NULL) {
        if (strcmp(head->word, info) == 0) {
            head->cnt++;
            return tmp_head;
        }
        head = head->next;
    }

    node_t *tmp = new_node(info);
    tmp_head = add_end(tmp_head, tmp);
    return tmp_head;
}

/**
 * compare : Gets two nodes and compares them first based on their cnt attribute and then on their word attribute.
 *
 * @param route1 : A pointer to the 1st node.
 * @param route2 : A pointer to the 2nd node.
 *
 * @return : -1 if the first node is bigger.
 *            1 if the 2nd node is bigger.
 *            0 if they are equal.
 *
 */


int compare(node_t *route1, node_t *route2) {
    if (route1->cnt > route2->cnt)
        return -1;
    else if (route1->cnt < route2->cnt)
        return 1;
    else
        return strcmp(route1->word, route2->word);
}

/**
 * sort : Sorts the whole list using the compare function above.
 *
 * @param list : A reference pointer to the head of the list.
 *
 */

void sort(node_t **list) {
    node_t *head = *list;
    node_t *sorted = NULL;

    while (head != NULL) {
        node_t *current = head;
        head = head->next;

        if (sorted == NULL || compare(current, sorted) < 0) {
            current->next = sorted;
            sorted = current;
        }

        else {
            node_t *p = sorted;
            while (p->next != NULL && compare(current, p->next) >= 0)
                p = p->next;
            current->next = p->next;
            p->next = current;
        }
    }
    *list = sorted;
}

/**
 * escapeQuotes : It deletes the " from the string.
 *
 * @param str : The string that we want to remove the " from.
 *
 */

char* escapeQuotes(char *str) {
    char *escaped_str = malloc(strlen(str) * 2 + 1);
    int j = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '\"') {
            escaped_str[j++] = '\"';
        }
        escaped_str[j++] = str[i];
    }
    escaped_str[j] = '\0';
    return escaped_str;
}

/**
 * removeChar : It deletes ' characters from a string.
 *
 * @param str : The string that needs to be corrected.
 *
 * @return : The resulting string.
 *
 */

char* removeChar(char str[]) {
    int len = strlen(str);
    int i, j;
    for (i = 0, j = 0; i < len; i++) {
        if (str[i] != '\'') {
            str[j] = str[i];
            j++;
        }
    }
    str[j] = '\0';
    return str;
}

/**
 * writeCSV : It will write the first n nodes from the list to csv file.
 *
 * @param head : A pointer to the head of the list.
 * @param n : The number of items that we want to write in the csv file.
 *
 */

void writeCSV(node_t *head, int n) {
    FILE *file;
    file = fopen("output.csv", "w");
    fprintf(file, "subject,statistic\n");
    for (int i = 1; i <= n; i++) {
        fprintf(file, "\"%s\",%d\n", escapeQuotes(head->word), head->cnt);
        head = head->next;
    }
}

/**
 * removeLeadingWhitespace : It will erase the leading whitespaces from the given string.
 *
 * @param data : the string that we want to remove the leading whitespace from.
 *
 * @return : The corrected string.
 *
 */

char* removeLeadingWhitespace(char data[]) {
    int ind = 0, flag = 0;
    char *tmp = (char *)malloc(sizeof(char) * strlen(data));
    for (int i = 0; i < strlen(data); i++) {
        char c = data[i];
        if (c == ' ' && flag == 0)
            continue;
        else if (c != ' ')
            flag = 1;
        tmp[ind] = c;
        ind++;
    }
    tmp[ind] = '\0';
    return tmp;
}

/**
 * solveQ1 : This function solves the first question.
 *
 * @param data : the filename.
 * @param n : The number of lines needed in the output csv file.
 *
 */


void solveQ1(char data[], int n) {
    node_t *routes = NULL;
    char *line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    FILE* file = fopen(data, "r");
    char *airline_name = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    char *airline_icao_unique_code = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    char *dest_country = (char *)malloc(sizeof(char) * MAX_LINE_LEN); 
    int line_cnt = 0;
    while (fgets(line, MAX_LINE_LEN, file) != NULL) {
        line[strcspn(line, "\r\n")] = '\0';
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(sizeof(char) * strlen(token));
        if (token[0] == '-') {
            line_cnt = 0;
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(airline_name, tmp);
        }
        else if (line_cnt == 1) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(airline_icao_unique_code, tmp);
        }
        else if (line_cnt == 10) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(dest_country, tmp);
            if (!strcmp(dest_country, "Canada")) {
                strcat(airline_name, " (");
                strncat(airline_icao_unique_code, ")", 1);
                strcat(airline_name, airline_icao_unique_code);
                routes = addValue(routes, airline_name);

            }
        }
        free(tmp);
        line_cnt ++;
    }
    free(airline_name);
    free(airline_icao_unique_code);
    free(dest_country);
    free(line);
    fclose(file);
    sort(&routes);
    writeCSV(routes, n);
}

/**
 * solveQ2 : This function solves the first question.
 *
 * @param data : the filename.
 * @param n : The number of lines needed in the output csv file.
 *
 */


void solveQ2(char data[], int n) {
    node_t *routes = NULL;
    char *line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    FILE* file = fopen(data, "r");
    char *dest_country = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    int line_cnt = 0;
    while (fgets(line, MAX_LINE_LEN, file) != NULL) {
        line[strcspn(line, "\r\n")] = '\0';
        if (!strcmp(line, "routes:"))
            continue;
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(sizeof(char) * strlen(token));
        if (line_cnt == 10) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(dest_country, tmp);
            routes = addValue(routes, dest_country);
        }
        line_cnt ++;
        if (line_cnt == 13)     line_cnt = 0;
        free(tmp);
    }
    node_t *head = routes;
    routes = head;

    free(dest_country);
    free(line);
    fclose(file);
    while (routes != NULL) {
        routes->cnt *= -1;
        routes = routes->next;
    }
    routes = head;
    sort(&routes);
    head = routes;
    while (routes != NULL) {
        routes->cnt *= -1;
        routes = routes->next;
    }
    routes = head;
    writeCSV(routes, n);
}

/**
 * solveQ3 : This function solves the first question.
 *
 * @param data : the filename.
 * @param n : The number of lines needed in the output csv file.
 *
 */

void solveQ3(char data[], int n) {
    node_t *routes = NULL;
    char *line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    FILE* file = fopen(data, "r");
    char *to_airport_name = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    char *to_airport_icao_unique_code = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    char *to_airport_city = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    char *to_airport_country = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    int line_cnt = 0;
    while (fgets(line, MAX_LINE_LEN, file) != NULL) {
        line[strcspn(line, "\r\n")] = '\0';
        if (!strcmp(line, "routes:"))
            continue;
        char *token = strtok(line, ":");
        char *tmp = (char *)malloc(sizeof(char) * strlen(token));
        if (line_cnt == 8) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(to_airport_name, tmp);
        }
        else if (line_cnt == 9) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(to_airport_city, tmp);
        }
        else if (line_cnt == 10) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(to_airport_country, tmp);
        }
        else if (line_cnt == 11) {
            token = strtok(NULL, "");
            tmp = removeChar(token);
            tmp = removeLeadingWhitespace(tmp);
            strcpy(to_airport_icao_unique_code, tmp);
            strcat(to_airport_name, " (");
            strcat(to_airport_name, to_airport_icao_unique_code);
            strcat(to_airport_name, "), ");
            strcat(to_airport_name, to_airport_city);
            strcat(to_airport_name, ", ");
            strcat(to_airport_name, to_airport_country);
            routes = addValue(routes, to_airport_name);
        }
        line_cnt ++;
        if (line_cnt == 13)     line_cnt = 0;
    }
    free(line);
    free(to_airport_name);
    free(to_airport_icao_unique_code);
    free(to_airport_city);
    free(to_airport_country);
    fclose(file);
    sort(&routes);
    writeCSV(routes, n);
}


/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */

int main(int argc, char *argv[]) {
    // Fixing the Input
    for (int i = 1; i <= 3; i++)
        fixInput(argv[i]);
    int Q = atoi(argv[2]);
    int N = atoi(argv[3]);
    if (Q == 1)
        solveQ1(argv[1], N);
    if (Q == 2)
        solveQ2(argv[1], N);
    if (Q == 3)
        solveQ3(argv[1], N);
    exit(0);
}
