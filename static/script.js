window.onload = function() {
    let addRowButton = document.getElementById('add-row');
    addRowButton.addEventListener('click', function(e){
        e.preventDefault();
        let allFormsWrapper = document.getElementById('forms');
        let allAssignmentsField = document.getElementsByName('assignments');
        let allGradesField = document.getElementsByName('grades')
        let allWeightsField = document.getElementsByName('weights')


        let assignmentInputIds = [];
        for (let i = 0; i < allAssignmentsField.length; i++) {
            assignmentInputIds.push(i)
        }
        
        let gradeInputIds = [];
        for (let i = 0; i < allGradesField.length; i++) {
            gradeInputIds.push(i)
        }

        let weightInputIds = [];
        for (let i = 0; i < allWeightsField.length; i++) {
            weightInputIds.push(i)
        }


        let newAssignmentFieldName = `assignments-${Math.max(...assignmentInputIds)+1}`;
        let newGradesFieldName = `grades-${Math.max(...gradeInputIds)+1}`;
        let newWeightsFieldName = `weights-${Math.max(...weightInputIds)+1}`;
        
        let newField = `<tr><td id="${newAssignmentFieldName}" name="assignments"><input type="text" name="assignments"></td>
            <td id="${newGradesFieldName}" name="grades"><input type="text" name="grades"></td>
            <td id="${newWeightsFieldName}" name="weights"><input type="text" name="weights"></td></tr>`

        allFormsWrapper.insertAdjacentHTML('beforeend', newField);

    
    });
}