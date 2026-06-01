#!/bin/bash

mutation_killed=0
total_mutation=0
sample="sample_program.py"

cp "$sample" temp_sample_program.py


#==== Complete the code below ===============================================

# 1. Generate mutation files from the sample program
#    (use the provided mutator script)
python3 mutator-starter.py sample_program.py 


# 2. Loop over each generated mutation file and run test on the mutation file
#    Don't forget to:
#      - clear pytest caches
#      - run pytest with --clear-cache -v flags
for file in mutation_*.py; do
    echo "$file"
    #complete the code below


    total_mutation=$((total_mutation + 1))

    rm -rf __pycache__
    rm -rf .pytest_cache

    cp $file $sample # notice that "cp" does not delete the $file after finished, but "mv" does. :)

    if ! pytest --cache-clear -v test_sample_program.py; then # pytest fail คือ mutant ถูกฆ่า หรือก็คือ test case เราดี
        mutation_killed=$((mutation_killed + 1))
    fi
    cp temp_sample_program.py "$sample" 
done


#==== End of your code =======================================================

# Guard against division by zero
if [ "$total_mutation" -eq 0 ]; then
    echo "Mutation score: 0.00 (no mutations generated)"
    exit 0
fi

mutation_score=$(echo "scale=2; $mutation_killed / $total_mutation" | bc)
echo "Mutation score: $mutation_score"

