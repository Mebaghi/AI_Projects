# Est -> [1: 0 - 10], [2: 10-30], [3: 30-60], [4: x > 60]
# satisfaction <- WillWait

train_instances = {
    'x1':
        {
            'Alt': 'True',
            'Bar': 'False',
            'Fri': 'False',
            'Hun': 'True',
            'Pat': 'Some',
            'Price': '$$$',
            'Rain': 'False',
            'Res': 'True',
            'Type': 'French',
            'Est': '1',
            'satisfaction': 'True'
        },
    'x2':
        {
            'Alt': 'True',
            'Bar': 'False',
            'Fri': 'False',
            'Hun': 'True',
            'Pat': 'Full',
            'Price': '$',
            'Rain': 'False',
            'Res': 'False',
            'Type': 'Thai',
            'Est': '2',
            'satisfaction': 'False'
        },
    'x3':
        {
            'Alt': 'False',
            'Bar': 'True',
            'Fri': 'False',
            'Hun': 'False',
            'Pat': 'Some',
            'Price': '$',
            'Rain': 'False',
            'Res': 'False',
            'Type': 'Burger',
            'Est': '1',
            'satisfaction': 'True'
        },
    'x4':
        {
            'Alt': 'True',
            'Bar': 'False',
            'Fri': 'True',
            'Hun': 'True',
            'Pat': 'Full',
            'Price': '$',
            'Rain': 'True',
            'Res': 'False',
            'Type': 'Thai',
            'Est': '2',
            'satisfaction': 'True'
        },
    'x5':
        {
            'Alt': 'True',
            'Bar': 'False',
            'Fri': 'True',
            'Hun': 'False',
            'Pat': 'Full',
            'Price': '$$$',
            'Rain': 'False',
            'Res': 'True',
            'Type': 'French',
            'Est': '4',
            'satisfaction': 'False'
        },
    'x6':
        {
            'Alt': 'False',
            'Bar': 'True',
            'Fri': 'False',
            'Hun': 'True',
            'Pat': 'Some',
            'Price': '$$',
            'Rain': 'True',
            'Res': 'True',
            'Type': 'Italian',
            'Est': '1',
            'satisfaction': 'True'
        },
    'x7':
        {
            'Alt': 'False',
            'Bar': 'True',
            'Fri': 'False',
            'Hun': 'False',
            'Pat': 'None',
            'Price': '$',
            'Rain': 'True',
            'Res': 'False',
            'Type': 'Burger',
            'Est': '1',
            'satisfaction': 'False'
        },
    'x8':
        {
            'Alt': 'False',
            'Bar': 'False',
            'Fri': 'False',
            'Hun': 'True',
            'Pat': 'Some',
            'Price': '$$',
            'Rain': 'True',
            'Res': 'False',
            'Type': 'Thai',
            'Est': '1',
            'satisfaction': 'True'
        },
    'x9':
        {
            'Alt': 'False',
            'Bar': 'True',
            'Fri': 'True',
            'Hun': 'False',
            'Pat': 'Full',
            'Price': '$',
            'Rain': 'True',
            'Res': 'False',
            'Type': 'Burger',
            'Est': '4',
            'satisfaction': 'False'
        },
    'x10':
        {
            'Alt': 'True',
            'Bar': 'True',
            'Fri': 'True',
            'Hun': 'True',
            'Pat': 'Full',
            'Price': '$$',
            'Rain': 'False',
            'Res': 'True',
            'Type': 'Italian',
            'Est': '2',
            'satisfaction': 'False'
        },

}


test_instances = {
    'x11':
        {
            'Alt': 'False',
            'Bar': 'False',
            'Fri': 'False',
            'Hun': 'False',
            'Pat': 'None',
            'Price': '$',
            'Rain': 'False',
            'Res': 'False',
            'Type': 'Thai',
            'Est': '1',
            'satisfaction': 'False'
        },
    'x12':
        {
            'Alt': 'True',
            'Bar': 'True',
            'Fri': 'True',
            'Hun': 'True',
            'Pat': 'Full',
            'Price': '$',
            'Rain': 'False',
            'Res': 'False',
            'Type': 'Burger',
            'Est': '3',
            'satisfaction': 'True'
        }
}
