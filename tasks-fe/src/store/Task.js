import { makeAutoObservable, reaction } from "mobx"

export class Task {
    pk = null;
    title = "";
    complete = null;
    start = null;
    due = null;
    description = "";

    store = null;

    constructor (store, pk) {
        makeAutoObservable(this, {
            pk: false,
            store: false,
            saveHandler: false,
            dispose: false
        });
        // Could do validations here too if I wanted...
        this.store = store;
        this.pk = pk;

        this.saveHandler = reaction(
            () => this.asJson, // Observe everything used in the JSON
            json => {
                // If autosave is true, send JSON to update server
                if (this.autoSave) {
                    this.store.API.saveTask(json);
                }
            });
    }

    delete() {
        this.store.API.deleteTask(this.pk);
        this.store.remove(this);
    }

    get asJson() {
        return {
            pk: this.pk,
            title: this.title,
            complete: this.complete,
            start: this.start, 
            due: this.due,
            description: this.description
        };
    }

    toggleComplete () {
        this.store.API.toggleComplete(this.pk);
        this.complete = !this.complete;
    }

    // Update todo with info from server
    updateFromJson(json) {
        this.autoSave = false;
        // Prevent sending these changes back to the server
        this.title = json.title;
        this.complete = json.complete;
        this.start = json.start;
        this.due = json.due;
        this.description = json.description;
        this.autoSave = true;
    }

    dispose () {
        // Call this if the object is not needed but not deleted
        this.saveHandler();
    }
}