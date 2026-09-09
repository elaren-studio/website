import { test } from 'node:test';
import assert from 'node:assert/strict';
import { providerAccepted, submitInquiry, INQUIRY_ENDPOINT } from '../src/lib/inquiry.ts';

test('only a confirmed submission is accepted, not activation or an arbitrary 200', () => {
  for (const response of [null, {}, {success: false}, {success: 'false'}, {success: true, message: 'Please activate your form'}, {success: 'true'}]) {
    assert.equal(providerAccepted(response), false);
  }
  for (const success of [true, 'true']) assert.equal(providerAccepted({success, message: 'The form was submitted successfully.'}), true);
});

test('submits once with JSON and preserves the inquiry payload', async () => {
  const payload = {name: 'Synthetic test', message: 'A & B\nLine two', 'Source page': '/local-seo/'};
  let calls = 0;
  await submitInquiry(payload, (async (url, options) => {
    calls++;
    assert.equal(url, INQUIRY_ENDPOINT);
    assert.equal(options?.method, 'POST');
    assert.deepEqual(JSON.parse(String(options?.body)), payload);
    assert.ok(options?.signal);
    return new Response(JSON.stringify({success: 'true', message: 'The form was submitted successfully.'}));
  }) as typeof fetch);
  assert.equal(calls, 1);
});

test('network, HTTP, malformed JSON and unconfirmed responses fail without automatic retries', async () => {
  for (const result of [new Error('offline'), new Response('{}', {status: 503}), new Response('not JSON'), new Response(JSON.stringify({success: true, message: 'Activate the form'}))]) {
    let calls = 0;
    await assert.rejects(submitInquiry({message: 'Retain me'}, (async () => {
      calls++;
      if (result instanceof Error) throw result;
      return result;
    }) as typeof fetch));
    assert.equal(calls, 1);
  }
});
