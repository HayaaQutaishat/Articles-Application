document.addEventListener('DOMContentLoaded', function() {

    const one = document.querySelector('#first')
    const two = document.querySelector('#second')
    const three = document.querySelector('#third')
    const four = document.querySelector('#fourth')
    const five = document.querySelector('#fifth')

    const form = document.querySelector('.rate-form')

    const handleSelection = (selection) => {
        switch(selection) {
            case 'first': {
                one.classList.add('checked')
                two.classList.remove('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return 
            }
            case 'second': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case 'third': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case 'fourth': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.remove('checked')
                return
            }
            case 'fifth': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked')
                return
            }
        }
    }
    const arr = [one, two, three, four, five]

    arr.forEach(item => item.addEventListener('mouseover', (event)=> {
        handleSelection(event.target.id)
    }))
    arr.forEach(item => item.addEventListener('click', (event)=> {
        // grab the id of the clicked star
        const val = event.target.id;
        form.addEventListener('submit', e=> {
            e.preventDefault()
            // grab the id of the rated article 
            const id = e.target.id
            console.log(id)


            fetch('/rating', {
                method: 'POST',
                body: JSON.stringify({
                    id: id,
                })
              })
              .then(response => response.json())
              .then(result => {
                  // Print result
                  console.log(result);
              });

        })
    }))
})

