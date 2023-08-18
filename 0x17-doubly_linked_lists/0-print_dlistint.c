#include "lists.h"

/**
 * print_dlistint-  prints all the elements of a list.
 * @h: the header
 * Return: the number of nodes.
 */
size_t print_dlistint(const dlistint_t *h);
{
	int count;

	size_t count = 0;

	if (h != NULL)
	{
		printf("%d\n". h->n);
		count++;
		h = h->next;
	}

	return (count);
}
