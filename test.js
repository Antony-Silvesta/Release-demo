const { assert } = await import('chai');

describe('Simple Test Suite', function() {
    it('should pass a test', function() {
        assert.isTrue(true);
    });

    it('should add numbers correctly', function() {
        assert.equal(1 + 1, 2);
    });
});
