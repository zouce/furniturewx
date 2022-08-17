export class Test {
    constructor(id, AcWingOS) {
        this.$ac_game = $('#' + id);
        this.$playground = $(`<div class="ac-game-playground">success</div>`);
        this.start();
        this.$ac_game.append(this.$playground);
    }

    start() {
        this.$playground.show();
    }
}

