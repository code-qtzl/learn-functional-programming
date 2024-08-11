from functools import reduce # importing reduce function


def lines_with_sequence(char):
    def with_char(length):
        # Generate the sequence by repeating the character `char` for `length` times
        sequence = char * length
        # This function takes the document string and counts lines containing the `sequence`
        def with_length(doc):
            # Split the document into lines
            lines = doc.split('\n')

            # Define a function to check if a line contains the sequence
            def contains_sequence(count, line):
                # Increment count if the sequence is found in the line, otherwise keep count unchanged
                return count + (1 if sequence in line else 0)
            
            # Use reduce to count lines containing the sequence
            num_lines = reduce(contains_sequence, lines, 0)
            
            return num_lines

        return with_length

    return with_char