"""Training Exercise: Working with Nested Data Structures.

Developer Best Practices:
    Make small, frequent commits as you reach milestones. This is a crucial
    habit for professional developers. For example, once you solve the core
    problem, make a commit before starting the stretch goals. Good commit
    messages might be:
    - 'Loop and print asset_id and type for all assets'
    - 'Conditionally print headline for text assets'
    - 'Add counter for text and image asset types'

Focus:
    How to access data from nested dictionaries within a list.

Core Problem:
    Write a script that loops through the `CREATIVE_ASSETS` list below and
    prints the `asset_id` and `type` for each asset.

    Example Output for Core Problem:
    ID: img-001, Type: image
    ID: txt-002, Type: text
    ... (and so on for all assets)

Stretch Goals:
    1. For assets of type "text", also print the headline. You will need to
       access the nested 'data' dictionary to get this value.
    2. Create a count of how many "text" ads and "image" ads are in our
       list. Print the final counts at the end of the script.

    Example Output for Stretch Goals:
    ID: img-001, Type: image
    ID: txt-002, Type: text, Headline: Sign Up Today and Save!
    ID: img-003, Type: image
    ID: txt-004, Type: text, Headline: Limited Time Offer
    ---
    Total Image Assets: 2
    Total Text Assets: 2

"""

# --- DATA FOR THE EXERCISE ---

CREATIVE_ASSETS = [
    {
        'asset_id': 'img-001',
        'type': 'image',
        'data': {
            'url': 'https://example.com/image1.jpg',
            'alt_text': 'A beautiful mountain landscape.'
        }
    },
    {
        'asset_id': 'txt-002',
        'type': 'text',
        'data': {
            'headline': 'Sign Up Today and Save!',
            'description': 'Join our newsletter for 20% off your first order.'
        }
    },
    {
        'asset_id': 'img-003',
        'type': 'image',
        'data': {
            'url': 'https://example.com/image2.png',
            'alt_text': 'A modern company logo.'
        }
    },
    {
        'asset_id': 'txt-004',
        'type': 'text',
        'data': {
            'headline': 'Limited Time Offer',
            'description': 'Don\'t miss out on our seasonal specials.'
        }
    }
]


# --- WRITE YOUR CODE BELOW ---
