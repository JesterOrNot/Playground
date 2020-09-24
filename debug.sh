#!/bin/bash

python3 trie.py | sed "s/'/\"/g" | jq
