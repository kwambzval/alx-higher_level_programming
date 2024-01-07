#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int array[2048];
	int i = 0;
	int j;

	if (head == NULL || *head == NULL)
		return (1);

	while (temp != NULL)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (array[j] != array[i - 1 - j])
			return (0);
	}

	return (1);
}

