prependValue(valueToFind, newValue){
    if(this.contains(valueToFind)!=true) {
        return false;
    }
    else {
        var newNode = new SLNode(newValue);
        var finder = this.head;
        var lagger = null;
        while(finder != null) {
            if(finder==valueToFind && finder==this.head) {
                this.addToFront(newNode);
            }
            else if(finder==valueToFind) {
                lagger.next = newNode;
                newNode.next = finder;
                return this;
            }
            else {
                lagger = finder;
                finder = finder.next
                console.log(finder);
            }
        }
    }
    return this;
}
