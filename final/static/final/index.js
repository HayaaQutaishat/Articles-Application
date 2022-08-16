document.addEventListener('DOMContentLoaded', function() {

    const one = document.querySelector('#first')
    const two = document.querySelector('#second')
    const three = document.querySelector('#third')
    const four = document.querySelector('#fourth')
    const five = document.querySelector('#fifth')
    const form = document.querySelector('.rate-form')
    const confirmBox = document.getElementById('confirm-rating')

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

    // to convert btn id from string into integer :
    const getNumericValue = (stringValue) => {
        let numericValue;
        if (stringValue === 'first') {
            numericValue = 1;
        } else if (stringValue === 'second') {
            numericValue = 2;
        }  else if (stringValue === 'third') {
            numericValue = 3;
        }  else if (stringValue === 'fourth') {
            numericValue = 4;
        }  else if (stringValue === 'fifth') {
            numericValue = 5;
        } else {
            numericValue = 0;
        } return numericValue;
    }

    const arr = [one, two, three, four, five]

    arr.forEach(item => item.addEventListener('mouseover', (event)=> {
        handleSelection(event.target.id)
    }))
    arr.forEach(item => item.addEventListener('click', (event)=> {
        // grab the id of the clicked star (first,second,third   ,,,, )
        const val = event.target.id;
        // console.log(val)
        form.addEventListener('submit', e=> {
            e.preventDefault()
            // grab the id of the rated article 
            const id = e.target.id
            console.log(id)
            // grab the id of the score of the article
            const score = getNumericValue(val);
            console.log(score)
            fetch('/rating', {
                method: 'POST',
                body: JSON.stringify({
                    id: id,
                    score: score
                })
              })
              .then(response => response.json())
              .then(result => {
                //   console.log(result);
                confirmBox.innerHTML = `<p><mark>Successfully rated with ${score} star(s)!</mark></p>`
              });
        })
    }))

    const edit_btns = document.querySelectorAll('.edit_btn')
    edit_btns.forEach(btn => {
        btn.addEventListener('click', (event)=>{
            event.preventDefault()
            const comment_id = event.target.id;
            edit_comment(comment_id)
        })
      });


      function edit_comment(comment_id) {
        fetch('/commentt', {
            method: 'POST',
            body: JSON.stringify({
                comment_id: comment_id,
            })
          })
          .then(response => response.json())
          .then(comment => {
            //   alert(comment);
              let edit_comment_div = document.createElement('div');
              edit_comment_div.innerHTML = 
              `<form class="edit-form">
                <textarea id="new_comment" name="new_comment" autofocus" class="form-control" style=" min-width:500px; max-width:100%;min-height:50px;height:100%;width:100%;">${comment}</textarea><br>
                <input type="submit" value="Save" class="btn btn-primary"/>
              </form>`
              const comment_element = document.querySelector('#comment_view');
              comment_element.append(edit_comment_div);
              document.querySelector('.edit-form').addEventListener('submit',(e)=> {
                e.preventDefault()
                edit(comment_id)
              });
          });
        }
        function edit(comment_id) {
            const new_comment = document.querySelector('#new_comment').value;
            fetch('/edit_comment', {
              method: 'POST',
              body: JSON.stringify({
                new_comment: new_comment,
                comment_id: comment_id
              })
            })
            .then(response => response.json())
            .then(result => {
                // Print result
                location.reload();
                console.log(result);
            });
            return false; 
          }
        // Bootstrap Modal (Popup)
        var myModal = document.getElementById('myModal')
        var myInput = document.getElementById('myInput')
        myModal.addEventListener('shown.bs.modal', function () {
        myInput.focus()
        })
    })

